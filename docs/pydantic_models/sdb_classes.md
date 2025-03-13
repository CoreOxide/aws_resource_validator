# Sdb Classes

# AttributeTypeDef

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

# BatchDeleteAttributesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.DeletableItemTypeDef]
- **Required**: Yes


# BatchPutAttributesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.ReplaceableItemTypeDef]
- **Required**: Yes


# CreateDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletableItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.AttributeTypeDef]]


# DeleteAttributesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.AttributeTypeDef]]

### Expected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb_classes.UpdateConditionTypeDef]


# DeleteDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainMetadataRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainMetadataResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAttributesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ConsistentRead
- **Type**: typing.Optional[bool]


# GetAttributesResultTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb_classes.AttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb_classes.AttributeTypeDef]
- **Required**: Yes

### AlternateNameEncoding
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb_classes.PaginatorConfigTypeDef]


# ListDomainsRequestTypeDef

### MaxNumberOfDomains
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsResultTypeDef

### DomainNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
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


# PutAttributesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.ReplaceableAttributeTypeDef]
- **Required**: Yes

### Expected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb_classes.UpdateConditionTypeDef]


# ReplaceableAttributeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Replace
- **Type**: typing.Optional[bool]


# ReplaceableItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.ReplaceableAttributeTypeDef]
- **Required**: Yes


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


# SelectRequestPaginateTypeDef

### SelectExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ConsistentRead
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb_classes.PaginatorConfigTypeDef]


# SelectRequestTypeDef

### SelectExpression
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### ConsistentRead
- **Type**: typing.Optional[bool]


# SelectResultTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb_classes.ItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# UpdateConditionTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Exists
- **Type**: typing.Optional[bool]


