# Cloudfront Keyvaluestore Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteKeyRequest

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyRequestListItem

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeKeyValueStoreRequest

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyValueStoreResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyRequest

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ResponseMetadata'>
- **Required**: Yes


# ListKeysRequest

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListKeysRequestPaginate

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.PaginatorConfig]


# ListKeysResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ListKeysResponseListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeysResponseListItem

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutKeyRequest

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


# PutKeyRequestListItem

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PutKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ResponseMetadata'>
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


# UpdateKeysRequest

### KvsARN
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes

### Puts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.PutKeyRequestListItem]]

### Deletes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.DeleteKeyRequestListItem]]


# UpdateKeysResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_classes.ResponseMetadata'>
- **Required**: Yes


