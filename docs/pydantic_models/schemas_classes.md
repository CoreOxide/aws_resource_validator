# Schemas Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDiscovererRequest

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CrossAccount
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDiscovererResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscovererArn
- **Type**: <class 'str'>
- **Required**: Yes

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### CrossAccount
- **Type**: <class 'bool'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegistryRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRegistryResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDiscovererRequest

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistryRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### RegistryName
- **Type**: typing.Optional[str]


# DeleteSchemaRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaVersionRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeBindingRequest

### Language
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# DescribeCodeBindingRequestWait

### Language
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCodeBindingResponse

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDiscovererRequest

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDiscovererResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscovererArn
- **Type**: <class 'str'>
- **Required**: Yes

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### CrossAccount
- **Type**: <class 'bool'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRegistryRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRegistryResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSchemaRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# DiscovererSummary

### DiscovererArn
- **Type**: typing.Optional[str]

### DiscovererId
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### CrossAccount
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# GetCodeBindingSourceRequest

### Language
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# GetCodeBindingSourceResponse

### Body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# GetDiscoveredSchemaResponse

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### RegistryName
- **Type**: typing.Optional[str]


# GetResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# ListDiscoverersRequest

### DiscovererIdPrefix
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SourceArnPrefix
- **Type**: typing.Optional[str]


# ListDiscoverersRequestPaginate

### DiscovererIdPrefix
- **Type**: typing.Optional[str]

### SourceArnPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfig]


# ListDiscoverersResponse

### Discoverers
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.DiscovererSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegistriesRequest

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RegistryNamePrefix
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]


# ListRegistriesRequestPaginate

### RegistryNamePrefix
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfig]


# ListRegistriesResponse

### Registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.RegistrySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsRequestPaginate

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfig]


# ListSchemaVersionsResponse

### SchemaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SchemaVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SchemaNamePrefix
- **Type**: typing.Optional[str]


# ListSchemasRequestPaginate

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfig]


# ListSchemasResponse

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SchemaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutCodeBindingRequest

### Language
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# PutCodeBindingResponse

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# RegistrySummary

### RegistryArn
- **Type**: typing.Optional[str]

### RegistryName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# SchemaSummary

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### VersionCount
- **Type**: typing.Optional[int]


# SchemaVersionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchSchemaSummary

### RegistryName
- **Type**: typing.Optional[str]

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### SchemaVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.schemas_classes.SearchSchemaVersionSummary]]


# SearchSchemaVersionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchSchemasRequest

### Keywords
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchSchemasRequestPaginate

### Keywords
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfig]


# SearchSchemasResponse

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SearchSchemaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartDiscovererRequest

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDiscovererResponse

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# StopDiscovererRequest

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# StopDiscovererResponse

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDiscovererRequest

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CrossAccount
- **Type**: typing.Optional[bool]


# UpdateDiscovererResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DiscovererArn
- **Type**: <class 'str'>
- **Required**: Yes

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### CrossAccount
- **Type**: <class 'bool'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRegistryRequest

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRegistryResponse

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


