# Cloud9 Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEnvironmentEC2RequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### subnetId
- **Type**: typing.Optional[str]

### automaticStopTimeMinutes
- **Type**: typing.Optional[int]

### ownerArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloud9_classes.TagTypeDef]]

### connectionType
- **Type**: typing.Optional[typing.Literal['CONNECT_SSH', 'CONNECT_SSM']]

### dryRun
- **Type**: typing.Optional[bool]


# CreateEnvironmentEC2ResultTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentMembershipRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.Literal['read-only', 'read-write']
- **Required**: Yes


# CreateEnvironmentMembershipResultTypeDef

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentMemberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentMembershipRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEnvironmentMembershipsRequestPaginateTypeDef

### userArn
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['owner', 'read-only', 'read-write']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.PaginatorConfigTypeDef]


# DescribeEnvironmentMembershipsRequestTypeDef

### userArn
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['owner', 'read-only', 'read-write']]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeEnvironmentMembershipsResultTypeDef

### memberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEnvironmentStatusRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEnvironmentStatusResultTypeDef

### status
- **Type**: typing.Literal['connecting', 'creating', 'deleting', 'error', 'ready', 'stopped', 'stopping']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEnvironmentsRequestTypeDef

### environmentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeEnvironmentsResultTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentLifecycleTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]

### reason
- **Type**: typing.Optional[str]

### failureResource
- **Type**: typing.Optional[str]


# EnvironmentMemberTypeDef

### permissions
- **Type**: typing.Literal['owner', 'read-only', 'read-write']
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### lastAccess
- **Type**: typing.Optional[datetime.datetime]


# EnvironmentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListEnvironmentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsResultTypeDef

### environmentIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloud9_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloud9_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentMembershipRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.Literal['read-only', 'read-write']
- **Required**: Yes


# UpdateEnvironmentMembershipResultTypeDef

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentMemberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnvironmentRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### managedCredentialsAction
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]


