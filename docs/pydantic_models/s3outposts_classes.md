# s3outposts_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEndpointRequestRequestTypeDef

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


# CreateEndpointResultTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEndpointRequestRequestTypeDef

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.NetworkInterfaceTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.FailedReasonTypeDef]


# FailedReasonTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ListEndpointsRequestListEndpointsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.PaginatorConfigTypeDef]


# ListEndpointsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEndpointsResultTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.EndpointTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOutpostsWithS3RequestListOutpostsWithS3PaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.PaginatorConfigTypeDef]


# ListOutpostsWithS3RequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOutpostsWithS3ResultTypeDef

### Outposts
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.OutpostTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSharedEndpointsRequestListSharedEndpointsPaginateTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3outposts_classes.PaginatorConfigTypeDef]


# ListSharedEndpointsRequestRequestTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSharedEndpointsResultTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3outposts_classes.EndpointTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NetworkInterfaceTypeDef

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# OutpostTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


