# Pydantic Models in schemas_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDiscovererRequestRequestTypeDef

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


# CreateRegistryRequestRequestTypeDef

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


# CreateSchemaRequestRequestTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['JSONSchemaDraft4', 'OpenApi3']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSchemaResponseTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### VersionCreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDiscovererRequestRequestTypeDef

### DiscovererId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistryRequestRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### RegistryName
- **Type**: typing.Optional[str]


# DeleteSchemaRequestRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaVersionRequestRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeBindingRequestCodeBindingExistsWaitTypeDef

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


# DescribeCodeBindingRequestRequestTypeDef

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


# DescribeDiscovererRequestRequestTypeDef

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


# DescribeRegistryRequestRequestTypeDef

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


# DescribeSchemaRequestRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# DescribeSchemaResponseTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### VersionCreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ExportSchemaRequestRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: typing.Optional[str]


# ExportSchemaResponseTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCodeBindingSourceRequestRequestTypeDef

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


# GetDiscoveredSchemaRequestRequestTypeDef

### Events
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Type
- **Type**: typing.Literal['JSONSchemaDraft4', 'OpenApi3']
- **Required**: Yes


# GetDiscoveredSchemaResponseTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestRequestTypeDef

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


# ListDiscoverersRequestListDiscoverersPaginateTypeDef

### DiscovererIdPrefix
- **Type**: typing.Optional[str]

### SourceArnPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListDiscoverersRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRegistriesRequestListRegistriesPaginateTypeDef

### RegistryNamePrefix
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListRegistriesRequestRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RegistryNamePrefix
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]


# ListRegistriesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.RegistrySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchemaVersionsRequestListSchemaVersionsPaginateTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListSchemaVersionsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SchemaVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchemasRequestListSchemasPaginateTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# ListSchemasRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SchemaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# PutCodeBindingRequestRequestTypeDef

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


# PutResourcePolicyRequestRequestTypeDef

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

### SchemaArn
- **Type**: typing.Optional[str]

### SchemaName
- **Type**: typing.Optional[str]

### SchemaVersion
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['JSONSchemaDraft4', 'OpenApi3']]


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

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### SchemaVersion
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['JSONSchemaDraft4', 'OpenApi3']]


# SearchSchemasRequestRequestTypeDef

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


# SearchSchemasRequestSearchSchemasPaginateTypeDef

### Keywords
- **Type**: <class 'str'>
- **Required**: Yes

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.schemas_classes.PaginatorConfigTypeDef]


# SearchSchemasResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.schemas_classes.SearchSchemaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDiscovererRequestRequestTypeDef

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


# StopDiscovererRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDiscovererRequestRequestTypeDef

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


# UpdateRegistryRequestRequestTypeDef

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


# UpdateSchemaRequestRequestTypeDef

### RegistryName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientTokenId
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['JSONSchemaDraft4', 'OpenApi3']]


# UpdateSchemaResponseTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SchemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### VersionCreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.schemas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


