# Resource Groups Classes

# AccountSettingsTypeDef

### GroupLifecycleEventsDesiredStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### GroupLifecycleEventsStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'IN_PROGRESS']]

### GroupLifecycleEventsStatusMessage
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTagSyncTaskInputTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ResourceQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Configuration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemUnionTypeDef]]

### Criticality
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# CreateGroupOutputTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupTypeDef'>
- **Required**: Yes

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### GroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGroupInputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# DeleteGroupOutputTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailedResourceTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]


# GetAccountSettingsOutputTypeDef

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupConfigurationInputTypeDef

### Group
- **Type**: typing.Optional[str]


# GetGroupConfigurationOutputTypeDef

### GroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupInputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# GetGroupOutputTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupQueryInputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# GetGroupQueryOutputTypeDef

### GroupQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTagSyncTaskInputTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagSyncTaskOutputTypeDef

### GroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTagsInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagsOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupConfigurationItemOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GroupConfigurationItemUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GroupConfigurationParameterOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Optional[typing.List[str]]


# GroupConfigurationParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GroupConfigurationTypeDef

### Configuration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemOutputTypeDef]]

### ProposedConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemOutputTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATING']]

### FailureReason
- **Type**: typing.Optional[str]


# GroupFilterTypeDef

### Name
- **Type**: typing.Literal['configuration-type', 'criticality', 'display-name', 'owner', 'resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GroupIdentifierTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Criticality
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# GroupQueryTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes


# GroupResourcesInputTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GroupResourcesOutputTypeDef

### Succeeded
- **Type**: typing.List[str]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.FailedResourceTypeDef]
- **Required**: Yes

### Pending
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.PendingResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupTypeDef

### GroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Criticality
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ApplicationTag
- **Type**: typing.Optional[typing.Dict[str, str]]


# GroupingStatusesItemTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['GROUP', 'UNGROUP']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SKIPPED', 'SUCCESS']]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ListGroupResourcesInputPaginateTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# ListGroupResourcesInputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupResourcesItemTypeDef

### Identifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceIdentifierTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceStatusTypeDef]


# ListGroupResourcesOutputTypeDef

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.ListGroupResourcesItemTypeDef]
- **Required**: Yes

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceIdentifierTypeDef]
- **Required**: Yes

### QueryErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.QueryErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupingStatusesFilterTypeDef

### Name
- **Type**: typing.Literal['resource-arn', 'status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListGroupingStatusesInputPaginateTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ListGroupingStatusesFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# ListGroupingStatusesInputTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ListGroupingStatusesFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupingStatusesOutputTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### GroupingStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupingStatusesItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsInputPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# ListGroupsInputTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsOutputTypeDef

### GroupIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupIdentifierTypeDef]
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagSyncTasksFilterTypeDef

### GroupArn
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# ListTagSyncTasksInputPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ListTagSyncTasksFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# ListTagSyncTasksInputTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ListTagSyncTasksFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagSyncTasksOutputTypeDef

### TagSyncTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.TagSyncTaskItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingResourceTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# PutGroupConfigurationInputTypeDef

### Group
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemUnionTypeDef]]


# QueryErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION_STACK_INACTIVE', 'CLOUDFORMATION_STACK_NOT_EXISTING', 'CLOUDFORMATION_STACK_UNASSUMABLE_ROLE', 'RESOURCE_TYPE_NOT_SUPPORTED']]

### Message
- **Type**: typing.Optional[str]


# ResourceFilterTypeDef

### Name
- **Type**: typing.Literal['resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResourceIdentifierTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ResourceQueryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceStatusTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['PENDING']]


# ResponseMetadataTypeDef

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


# SearchResourcesInputPaginateTypeDef

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# SearchResourcesInputTypeDef

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchResourcesOutputTypeDef

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceIdentifierTypeDef]
- **Required**: Yes

### QueryErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.QueryErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartTagSyncTaskInputTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartTagSyncTaskOutputTypeDef

### GroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValue
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagSyncTaskItemTypeDef

### GroupArn
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### TaskArn
- **Type**: typing.Optional[str]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# UngroupResourcesInputTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UngroupResourcesOutputTypeDef

### Succeeded
- **Type**: typing.List[str]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.FailedResourceTypeDef]
- **Required**: Yes

### Pending
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.PendingResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAccountSettingsInputTypeDef

### GroupLifecycleEventsDesiredStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# UpdateAccountSettingsOutputTypeDef

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupInputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Criticality
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# UpdateGroupOutputTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupQueryInputTypeDef

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# UpdateGroupQueryOutputTypeDef

### GroupQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


