# resource_groups_classes

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

# CreateGroupInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemTypeDef]]


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


# DeleteGroupInputRequestTypeDef

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


# GetGroupConfigurationInputRequestTypeDef

### Group
- **Type**: typing.Optional[str]


# GetGroupConfigurationOutputTypeDef

### GroupConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupInputRequestTypeDef

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


# GetGroupQueryInputRequestTypeDef

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


# GetTagsInputRequestTypeDef

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


# GroupConfigurationItemTypeDef

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationParameterTypeDef]]


# GroupConfigurationParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GroupConfigurationTypeDef

### Configuration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemTypeDef]]

### ProposedConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATING']]

### FailureReason
- **Type**: typing.Optional[str]


# GroupFilterTypeDef

### Name
- **Type**: typing.Literal['configuration-type', 'resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GroupIdentifierTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupArn
- **Type**: typing.Optional[str]


# GroupQueryTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes


# GroupResourcesInputRequestTypeDef

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


# ListGroupResourcesInputListGroupResourcesPaginateTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# ListGroupResourcesInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### QueryErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.QueryErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsInputListGroupsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# ListGroupsInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PutGroupConfigurationInputRequestTypeDef

### Group
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_groups_classes.GroupConfigurationItemTypeDef]]


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

### Type
- **Type**: typing.Literal['CLOUDFORMATION_STACK_1_0', 'TAG_FILTERS_1_0']
- **Required**: Yes

### Query
- **Type**: <class 'str'>
- **Required**: Yes


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


# SearchResourcesInputRequestTypeDef

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchResourcesInputSearchResourcesPaginateTypeDef

### ResourceQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResourceQueryTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_groups_classes.PaginatorConfigTypeDef]


# SearchResourcesOutputTypeDef

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.ResourceIdentifierTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### QueryErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_groups_classes.QueryErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagInputRequestTypeDef

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


# UngroupResourcesInputRequestTypeDef

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


# UntagInputRequestTypeDef

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


# UpdateAccountSettingsInputRequestTypeDef

### GroupLifecycleEventsDesiredStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# UpdateAccountSettingsOutputTypeDef

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupInputRequestTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateGroupOutputTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_groups_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGroupQueryInputRequestTypeDef

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


