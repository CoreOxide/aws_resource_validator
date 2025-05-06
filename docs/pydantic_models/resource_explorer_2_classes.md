# Resource Explorer 2 Classes

# AssociateDefaultViewInput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateDefaultViewOutput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetViewError

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetViewInput

### ViewArns
- **Type**: typing.Optional[typing.List[str]]


# BatchGetViewOutput

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.BatchGetViewError]
- **Required**: Yes

### Views
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.View]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIndexInput

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateIndexOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateViewInput

### ViewName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SearchFilter]

### IncludedProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.IncludedProperty]]

### Scope
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateViewOutput

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIndexInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteViewInput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteViewOutput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountLevelServiceConfigurationOutput

### OrgConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.OrgConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDefaultViewOutput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# GetIndexOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedViewInput

### ManagedViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedViewOutput

### ManagedView
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ManagedView'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# GetViewInput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetViewOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# IncludedProperty

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# Index

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]


# ListIndexesForMembersInput

### AccountIdList
- **Type**: typing.List[str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIndexesForMembersInputPaginate

### AccountIdList
- **Type**: typing.List[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# ListIndexesForMembersOutput

### Indexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.MemberIndex]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndexesInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Regions
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]


# ListIndexesInputPaginate

### Regions
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# ListIndexesOutput

### Indexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.Index]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedViewsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ServicePrincipal
- **Type**: typing.Optional[str]


# ListManagedViewsInputPaginate

### ServicePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# ListManagedViewsOutput

### ManagedViews
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesInput

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SearchFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


# ListResourcesInputPaginate

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SearchFilter]

### ViewArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# ListResourcesOutput

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.Resource]
- **Required**: Yes

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedResourceTypesInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedResourceTypesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# ListSupportedResourceTypesOutput

### ResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SupportedResourceType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# ListViewsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListViewsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# ListViewsOutput

### Views
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ManagedView

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SearchFilter]

### IncludedProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.IncludedProperty]]

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


# MemberIndex

### AccountId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AGGREGATOR', 'LOCAL']]


# OrgConfiguration

### AWSServiceAccessStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ServiceLinkedRole
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Resource

### Arn
- **Type**: typing.Optional[str]

### LastReportedAt
- **Type**: typing.Optional[datetime.datetime]

### OwningAccountId
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResourceProperty]]

### Region
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]


# ResourceCount

### Complete
- **Type**: typing.Optional[bool]

### TotalResources
- **Type**: typing.Optional[int]


# ResourceProperty

### Data
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### LastReportedAt
- **Type**: typing.Optional[datetime.datetime]

### Name
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


# SearchFilter

### FilterString
- **Type**: <class 'str'>
- **Required**: Yes


# SearchInput

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


# SearchInputPaginate

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ViewArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.PaginatorConfig]


# SearchOutput

### Count
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResourceCount'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.Resource]
- **Required**: Yes

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SupportedResourceType

### ResourceType
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateIndexTypeInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AGGREGATOR', 'LOCAL']
- **Required**: Yes


# UpdateIndexTypeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateViewInput

### ViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SearchFilter]

### IncludedProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.IncludedProperty]]


# UpdateViewOutput

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.ResponseMetadata'>
- **Required**: Yes


# View

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.SearchFilter]

### IncludedProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_classes.IncludedProperty]]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Owner
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### ViewArn
- **Type**: typing.Optional[str]


