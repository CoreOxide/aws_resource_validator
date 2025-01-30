# cloud9_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEnvironmentEC2RequestRequestTypeDef

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


# CreateEnvironmentMembershipRequestRequestTypeDef

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


# DeleteEnvironmentMembershipRequestRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEnvironmentMembershipsRequestDescribeEnvironmentMembershipsPaginateTypeDef

### userArn
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['owner', 'read-only', 'read-write']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.PaginatorConfigTypeDef]


# DescribeEnvironmentMembershipsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEnvironmentStatusRequestRequestTypeDef

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


# DescribeEnvironmentsRequestRequestTypeDef

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

### type
- **Type**: typing.Literal['ec2', 'ssh']
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ownerArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### connectionType
- **Type**: typing.Optional[typing.Literal['CONNECT_SSH', 'CONNECT_SSM']]

### lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.EnvironmentLifecycleTypeDef]

### managedCredentialsStatus
- **Type**: typing.Optional[typing.Literal['DISABLED_BY_COLLABORATOR', 'DISABLED_BY_DEFAULT', 'DISABLED_BY_OWNER', 'ENABLED_BY_OWNER', 'ENABLED_ON_CREATE', 'FAILED_REMOVAL_BY_COLLABORATOR', 'FAILED_REMOVAL_BY_OWNER', 'PENDING_REMOVAL_BY_COLLABORATOR', 'PENDING_REMOVAL_BY_OWNER', 'PENDING_START_REMOVAL_BY_COLLABORATOR', 'PENDING_START_REMOVAL_BY_OWNER']]


# ListEnvironmentsRequestListEnvironmentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloud9_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsResultTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### environmentIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloud9_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentMembershipRequestRequestTypeDef

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


# UpdateEnvironmentRequestRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### managedCredentialsAction
- **Type**: typing.Optional[typing.Literal['DISABLE', 'ENABLE']]


