# Mediastore Data Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteObjectRequestRequestTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectRequestRequestTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectResponseTypeDef

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ContentLength
- **Type**: <class 'int'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetObjectRequestRequestTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Range
- **Type**: typing.Optional[str]


# GetObjectResponseTypeDef

### Body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ContentRange
- **Type**: <class 'str'>
- **Required**: Yes

### ContentLength
- **Type**: <class 'int'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ItemTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['FOLDER', 'OBJECT']]

### ETag
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### ContentType
- **Type**: typing.Optional[str]

### ContentLength
- **Type**: typing.Optional[int]


# ListItemsRequestListItemsPaginateTypeDef

### Path
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediastore_data_classes.PaginatorConfigTypeDef]


# ListItemsRequestRequestTypeDef

### Path
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListItemsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_data_classes.ItemTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutObjectRequestRequestTypeDef

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### CacheControl
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[typing.Literal['TEMPORAL']]

### UploadAvailability
- **Type**: typing.Optional[typing.Literal['STANDARD', 'STREAMING']]


# PutObjectResponseTypeDef

### ContentSHA256
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### StorageClass
- **Type**: typing.Literal['TEMPORAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadataTypeDef'>
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


