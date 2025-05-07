# Resource Groups Classes

# AccountSettings

### GroupLifecycleEventsDesiredStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### GroupLifecycleEventsStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'IN_PROGRESS']]

### GroupLifecycleEventsStatusMessage
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTagSyncTaskInput

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ResourceQuery
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Configuration
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationItem, aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationItemOutput]]]

### Criticality
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# CreateGroupOutput

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.Group'>
- **Required**: Yes

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceQuery'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### GroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGroupInput

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# DeleteGroupOutput

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# FailedResource

### ResourceArn
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]


# GetAccountSettingsOutput

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupConfigurationInput

### Group
- **Type**: typing.Optional[str]


# GetGroupConfigurationOutput

### GroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupInput

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# GetGroupOutput

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupQueryInput

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# GetGroupQueryOutput

### GroupQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# GetTagSyncTaskInput

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagSyncTaskOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# GetTagsInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagsOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# Group

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


# GroupConfiguration

### Configuration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationItemOutput]]

### ProposedConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationItemOutput]]

### Status
- **Type**: typing.Optional[typing.Literal['UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATING']]

### FailureReason
- **Type**: typing.Optional[str]


# GroupConfigurationItem

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationParameter, aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationParameterOutput]]]


# GroupConfigurationItemOutput

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationParameterOutput]]


# GroupConfigurationParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Optional[typing.List[str]]


# GroupConfigurationParameterOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Optional[typing.List[str]]


# GroupFilter

### Name
- **Type**: typing.Literal['configuration-type', 'criticality', 'display-name', 'owner', 'resource-type']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# GroupIdentifier

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


# GroupQuery

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceQuery'>
- **Required**: Yes


# GroupResourcesInput

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes


# GroupResourcesOutput

### Succeeded
- **Type**: typing.List[str]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.FailedResource]
- **Required**: Yes

### Pending
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PendingResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# GroupingStatusesItem

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


# ListGroupResourcesInput

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupResourcesInputPaginate

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PaginatorConfig]


# ListGroupResourcesItem

### Identifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceIdentifier]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceStatus]


# ListGroupResourcesOutput

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ListGroupResourcesItem]
- **Required**: Yes

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceIdentifier]
- **Required**: Yes

### QueryErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.QueryError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupingStatusesFilter

### Name
- **Type**: typing.Literal['resource-arn', 'status']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ListGroupingStatusesInput

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ListGroupingStatusesFilter]]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupingStatusesInputPaginate

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ListGroupingStatusesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PaginatorConfig]


# ListGroupingStatusesOutput

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### GroupingStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupingStatusesItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsInput

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsInputPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PaginatorConfig]


# ListGroupsOutput

### GroupIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupIdentifier]
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.Group]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagSyncTasksFilter

### GroupArn
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# ListTagSyncTasksInput

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ListTagSyncTasksFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagSyncTasksInputPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ListTagSyncTasksFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PaginatorConfig]


# ListTagSyncTasksOutput

### TagSyncTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.TagSyncTaskItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingResource

### ResourceArn
- **Type**: typing.Optional[str]


# PutGroupConfigurationInput

### Group
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationItem, aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupConfigurationItemOutput]]]


# QueryError

### ErrorCode
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION_STACK_INACTIVE', 'CLOUDFORMATION_STACK_NOT_EXISTING', 'CLOUDFORMATION_STACK_UNASSUMABLE_ROLE', 'RESOURCE_TYPE_NOT_SUPPORTED']]

### Message
- **Type**: typing.Optional[str]


# ResourceFilter

### Name
- **Type**: typing.Literal['resource-type']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ResourceIdentifier

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ResourceQuery

### Type
- **Type**: typing.Literal['CLOUDFORMATION_STACK_1_0', 'TAG_FILTERS_1_0']
- **Required**: Yes

### Query
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceStatus

### Name
- **Type**: typing.Optional[typing.Literal['PENDING']]


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


# SearchResourcesInput

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceQuery'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchResourcesInputPaginate

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceQuery'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PaginatorConfig]


# SearchResourcesOutput

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceIdentifier]
- **Required**: Yes

### QueryErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.QueryError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartTagSyncTaskInput

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


# StartTagSyncTaskOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# TagInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# TagSyncTaskItem

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


# UngroupResourcesInput

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes


# UngroupResourcesOutput

### Succeeded
- **Type**: typing.List[str]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.FailedResource]
- **Required**: Yes

### Pending
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.PendingResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# UntagInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAccountSettingsInput

### GroupLifecycleEventsDesiredStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# UpdateAccountSettingsOutput

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGroupInput

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


# UpdateGroupOutput

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGroupQueryInput

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResourceQuery'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]


# UpdateGroupQueryOutput

### GroupQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.GroupQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups.resource_groups_classes.ResponseMetadata'>
- **Required**: Yes


