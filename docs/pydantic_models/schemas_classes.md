# Schemas Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDiscovererRequestTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CrossAccount
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDiscovererResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegistryRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRegistryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDiscovererRequestTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistryRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### RegistryName
- **Type**: typing.Optional[str]


# DeleteSchemaRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaVersionRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeBindingRequestTypeDef

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


# DescribeCodeBindingRequestWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.WaiterConfigTypeDef]


# DescribeCodeBindingResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDiscovererRequestTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDiscovererResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRegistryRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRegistryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSchemaRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# DiscovererSummaryTypeDef

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


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCodeBindingSourceRequestTypeDef

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


# GetCodeBindingSourceResponseTypeDef

### Body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDiscoveredSchemaResponseTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestTypeDef

### RegistryName
- **Type**: typing.Optional[str]


# GetResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDiscoverersRequestPaginateTypeDef

### DiscovererIdPrefix
- **Type**: typing.Optional[str]

### SourceArnPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListDiscoverersRequestTypeDef

### DiscovererIdPrefix
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SourceArnPrefix
- **Type**: typing.Optional[str]


# ListDiscoverersResponseTypeDef

### Discoverers
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.DiscovererSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegistriesRequestPaginateTypeDef

### RegistryNamePrefix
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListRegistriesRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RegistryNamePrefix
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]


# ListRegistriesResponseTypeDef

### Registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.RegistrySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaVersionsRequestPaginateTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListSchemaVersionsRequestTypeDef

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


# ListSchemaVersionsResponseTypeDef

### SchemaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SchemaVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasRequestPaginateTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListSchemasRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SchemaNamePrefix
- **Type**: typing.Optional[str]


# ListSchemasResponseTypeDef

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SchemaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutCodeBindingRequestTypeDef

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


# PutCodeBindingResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistrySummaryTypeDef

### RegistryArn
- **Type**: typing.Optional[str]

### RegistryName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# SchemaSummaryTypeDef

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


# SchemaVersionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchSchemaSummaryTypeDef

### RegistryName
- **Type**: typing.Optional[str]

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### SchemaVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.schemas_classes.SearchSchemaVersionSummaryTypeDef]]


# SearchSchemaVersionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchSchemasRequestPaginateTypeDef

### Keywords
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# SearchSchemasRequestTypeDef

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


# SearchSchemasResponseTypeDef

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SearchSchemaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartDiscovererRequestTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDiscovererResponseTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDiscovererRequestTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# StopDiscovererResponseTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDiscovererRequestTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CrossAccount
- **Type**: typing.Optional[bool]


# UpdateDiscovererResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRegistryRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRegistryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


