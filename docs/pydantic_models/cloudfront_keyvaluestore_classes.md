# Cloudfront Keyvaluestore Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteKeyRequestListItemTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyRequestRequestTypeDef

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyResponseTypeDef

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeKeyValueStoreRequestRequestTypeDef

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyValueStoreResponseTypeDef

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyRequestRequestTypeDef

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyResponseTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeysRequestListKeysPaginateTypeDef

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.PaginatorConfigTypeDef]


# ListKeysRequestRequestTypeDef

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListKeysResponseListItemTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListKeysResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ListKeysResponseListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutKeyRequestListItemTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PutKeyRequestRequestTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# PutKeyResponseTypeDef

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ResponseMetadataTypeDef'>
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


# UpdateKeysRequestRequestTypeDef

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes

### Puts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.PutKeyRequestListItemTypeDef]]

### Deletes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.DeleteKeyRequestListItemTypeDef]]


# UpdateKeysResponseTypeDef

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


