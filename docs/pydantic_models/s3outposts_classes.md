# S3Outposts Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEndpointRequest

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessType
- **Type**: typing.Optional[typing.Literal['CustomerOwnedIp', 'Private']]

### CustomerOwnedIpv4Pool
- **Type**: typing.Optional[str]


# CreateEndpointResult

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEndpointRequest

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### EndpointArn
- **Type**: typing.Optional[str]

### OutpostsId
- **Type**: typing.Optional[str]

### CidrBlock
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Available', 'Create_Failed', 'Delete_Failed', 'Deleting', 'Pending']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.NetworkInterface]]

### VpcId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupId
- **Type**: typing.Optional[str]

### AccessType
- **Type**: typing.Optional[typing.Literal['CustomerOwnedIp', 'Private']]

### CustomerOwnedIpv4Pool
- **Type**: typing.Optional[str]

### FailedReason
- **Type**: <class 'NoneType'>


# FailedReason

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ListEndpointsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEndpointsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.PaginatorConfig]


# ListEndpointsResult

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostsWithS3Request

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOutpostsWithS3RequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.PaginatorConfig]


# ListOutpostsWithS3Result

### Outposts
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.Outpost]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSharedEndpointsRequest

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSharedEndpointsRequestPaginate

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.PaginatorConfig]


# ListSharedEndpointsResult

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkInterface

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# Outpost

### OutpostArn
- **Type**: typing.Optional[str]

### S3OutpostArn
- **Type**: typing.Optional[str]

### OutpostId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### CapacityInBytes
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


