# Resource Explorer 2 Classes

# AssociateDefaultViewInputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateDefaultViewOutputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetViewErrorTypeDef

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetViewInputTypeDef

### ViewArns
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetViewOutputTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.BatchGetViewErrorTypeDef]
- **Required**: Yes

### Views
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.ViewTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIndexInputTypeDef

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIndexOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateViewInputTypeDef

### ViewName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SearchFilterTypeDef]

### IncludedProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_explorer_2_classes.IncludedPropertyTypeDef]]

### Scope
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateViewOutputTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIndexInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteViewInputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteViewOutputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccountLevelServiceConfigurationOutputTypeDef

### OrgConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.OrgConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDefaultViewOutputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetManagedViewInputTypeDef

### ManagedViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedViewOutputTypeDef

### ManagedView
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ManagedViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetViewInputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetViewOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IncludedPropertyTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# IndexTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListIndexesForMembersInputPaginateTypeDef

### AccountIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListIndexesForMembersInputTypeDef

### AccountIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIndexesForMembersOutputTypeDef

### Indexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.MemberIndexTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndexesOutputTypeDef

### Indexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.IndexTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedViewsInputPaginateTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListManagedViewsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ServicePrincipal
- **Type**: typing.Optional[str]


# ListManagedViewsOutputTypeDef

### ManagedViews
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesInputPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SearchFilterTypeDef]

### ViewArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListResourcesInputTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SearchFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


# ListResourcesOutputTypeDef

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResourceTypeDef]
- **Required**: Yes

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedResourceTypesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListSupportedResourceTypesInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedResourceTypesOutputTypeDef

### ResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SupportedResourceTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListViewsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListViewsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListViewsOutputTypeDef

### Views
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ManagedViewTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SearchFilterTypeDef]

### IncludedProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.IncludedPropertyTypeDef]]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ManagedViewArn
- **Type**: typing.Optional[str]

### ManagedViewName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### ResourcePolicy
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### TrustedService
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# MemberIndexTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrgConfigurationTypeDef

### AWSServiceAccessStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ServiceLinkedRole
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceCountTypeDef

### Complete
- **Type**: typing.Optional[bool]

### TotalResources
- **Type**: typing.Optional[int]


# ResourcePropertyTypeDef

### Data
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### LastReportedAt
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]


# ResourceTypeDef

### Arn
- **Type**: typing.Optional[str]

### LastReportedAt
- **Type**: typing.Optional[datetime.datetime]

### OwningAccountId
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResourcePropertyTypeDef]]

### Region
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]


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


# SearchFilterTypeDef

### FilterString
- **Type**: <class 'str'>
- **Required**: Yes


# SearchInputPaginateTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ViewArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# SearchInputTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


# SearchOutputTypeDef

### Count
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResourceCountTypeDef'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResourceTypeDef]
- **Required**: Yes

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SupportedResourceTypeTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateViewInputTypeDef

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SearchFilterTypeDef]

### IncludedProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resource_explorer_2_classes.IncludedPropertyTypeDef]]


# UpdateViewOutputTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ViewTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SearchFilterTypeDef]

### IncludedProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.IncludedPropertyTypeDef]]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Owner
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


