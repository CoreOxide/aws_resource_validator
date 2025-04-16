# Cloud9 Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEnvironmentEC2Request

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloud9_classes.Tag]]

### connectionType
- **Type**: typing.Optional[typing.Literal['CONNECT_SSH', 'CONNECT_SSM']]

### dryRun
- **Type**: typing.Optional[bool]


# CreateEnvironmentEC2Result

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentMembershipRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.Literal['read-only', 'read-write']
- **Required**: Yes


# CreateEnvironmentMembershipResult

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentMember'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentMembershipRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEnvironmentMembershipsRequest

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


# DescribeEnvironmentMembershipsRequestPaginate

### userArn
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['owner', 'read-only', 'read-write']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.PaginatorConfig]


# DescribeEnvironmentMembershipsResult

### memberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEnvironmentStatusRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEnvironmentStatusResult

### status
- **Type**: typing.Literal['connecting', 'creating', 'deleting', 'error', 'ready', 'stopped', 'stopping']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEnvironmentsRequest

### environmentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeEnvironmentsResult

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloud9_classes.Environment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes


# Environment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentLifecycle

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]

### reason
- **Type**: typing.Optional[str]

### failureResource
- **Type**: typing.Optional[str]


# EnvironmentMember

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


# ListEnvironmentsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.PaginatorConfig]


# ListEnvironmentsResult

### environmentIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloud9_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes


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


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloud9_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentMembershipRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.Literal['read-only', 'read-write']
- **Required**: Yes


# UpdateEnvironmentMembershipResult

### membership
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentMember'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnvironmentRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### managedCredentialsAction
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]


