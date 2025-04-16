# Mediastore Data Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteObjectRequest

### Path
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectRequest

### Path
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetObjectRequest

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Range
- **Type**: typing.Optional[str]


# GetObjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadata'>
- **Required**: Yes


# Item

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListItemsRequest

### Path
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListItemsRequestPaginate

### Path
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediastore_data_classes.PaginatorConfig]


# ListItemsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_data_classes.Item]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadata'>
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


# PutObjectRequest

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.Blob'>
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


# PutObjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_data_classes.ResponseMetadata'>
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


