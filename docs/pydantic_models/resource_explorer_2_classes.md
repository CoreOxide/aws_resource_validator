# Pydantic Models in resource_explorer_2_classes

# AssociateDefaultViewInputRequestTypeDef

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


# BatchGetViewInputRequestTypeDef

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


# CreateIndexInputRequestTypeDef

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


# CreateViewInputRequestTypeDef

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


# DeleteIndexInputRequestTypeDef

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


# DeleteViewInputRequestTypeDef

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


# GetIndexOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReplicatingFrom
- **Type**: typing.List[str]
- **Required**: Yes

### ReplicatingTo
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: typing.Literal['AGGREGATOR', 'LOCAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetViewInputRequestTypeDef

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

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]


# ListIndexesForMembersInputListIndexesForMembersPaginateTypeDef

### AccountIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListIndexesForMembersInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIndexesInputListIndexesPaginateTypeDef

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListIndexesInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]


# ListIndexesOutputTypeDef

### Indexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.IndexTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSupportedResourceTypesInputListSupportedResourceTypesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListSupportedResourceTypesInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedResourceTypesOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2_classes.SupportedResourceTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

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


# ListViewsInputListViewsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# ListViewsInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListViewsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Views
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MemberIndexTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]


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


# SearchFilterTypeDef

### FilterString
- **Type**: <class 'str'>
- **Required**: Yes


# SearchInputRequestTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


# SearchInputSearchPaginateTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ViewArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2_classes.PaginatorConfigTypeDef]


# SearchOutputTypeDef

### Count
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResourceCountTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
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


# SupportedResourceTypeTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIndexTypeInputRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AGGREGATOR', 'LOCAL']
- **Required**: Yes


# UpdateIndexTypeOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETING', 'UPDATING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['AGGREGATOR', 'LOCAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateViewInputRequestTypeDef

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


