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

# BatchDeleteAttributesRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.DeletableItemTypeDef]
- **Required**: Yes


# BatchPutAttributesRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.ReplaceableItemTypeDef]
- **Required**: Yes


# CreateDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletableItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sdb_classes.AttributeTypeDef]]


# DeleteAttributesRequestRequestTypeDef

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


# DeleteDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DomainMetadataRequestRequestTypeDef

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


# GetAttributesRequestRequestTypeDef

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


# ListDomainsRequestListDomainsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb_classes.PaginatorConfigTypeDef]


# ListDomainsRequestRequestTypeDef

### MaxNumberOfDomains
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsResultTypeDef

### DomainNames
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAttributesRequestRequestTypeDef

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


# SelectRequestRequestTypeDef

### SelectExpression
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### ConsistentRead
- **Type**: typing.Optional[bool]


# SelectRequestSelectPaginateTypeDef

### SelectExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ConsistentRead
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sdb_classes.PaginatorConfigTypeDef]


# SelectResultTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sdb_classes.ItemTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sdb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConditionTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Exists
- **Type**: typing.Optional[bool]


