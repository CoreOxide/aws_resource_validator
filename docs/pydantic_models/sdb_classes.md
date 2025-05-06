# Sdb Classes

# Attribute

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateNameEncoding
- **Type**: typing.Optional[str]

### AlternateValueEncoding
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteAttributesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.DeletableItem]
- **Required**: Yes


# BatchPutAttributesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.ReplaceableItem]
- **Required**: Yes


# CreateDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletableItem

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.Attribute]]


# DeleteAttributesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.Attribute]]

### Expected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb.sdb_classes.UpdateCondition]


# DeleteDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainMetadataRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainMetadataResult

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### ItemNamesSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### AttributeNameCount
- **Type**: <class 'int'>
- **Required**: Yes

### AttributeNamesSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### AttributeValueCount
- **Type**: <class 'int'>
- **Required**: Yes

### AttributeValuesSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb.sdb_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb.sdb_classes.ResponseMetadata'>
- **Required**: Yes


# GetAttributesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.List[str]]

### ConsistentRead
- **Type**: typing.Optional[bool]


# GetAttributesResult

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.Attribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb.sdb_classes.ResponseMetadata'>
- **Required**: Yes


# Item

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.Attribute]
- **Required**: Yes

### AlternateNameEncoding
- **Type**: typing.Optional[str]


# ListDomainsRequest

### MaxNumberOfDomains
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb.sdb_classes.PaginatorConfig]


# ListDomainsResult

### DomainNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb.sdb_classes.ResponseMetadata'>
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


# PutAttributesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.ReplaceableAttribute]
- **Required**: Yes

### Expected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb.sdb_classes.UpdateCondition]


# ReplaceableAttribute

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Replace
- **Type**: typing.Optional[bool]


# ReplaceableItem

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.ReplaceableAttribute]
- **Required**: Yes


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


# SelectRequest

### SelectExpression
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### ConsistentRead
- **Type**: typing.Optional[bool]


# SelectRequestPaginate

### SelectExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ConsistentRead
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb.sdb_classes.PaginatorConfig]


# SelectResult

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb.sdb_classes.Item]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb.sdb_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# UpdateCondition

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Exists
- **Type**: typing.Optional[bool]


