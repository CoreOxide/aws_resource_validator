# Mediastore Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerTypeDef

### Endpoint
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ARN
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]

### AccessLoggingEnabled
- **Type**: typing.Optional[bool]


# CorsRuleTypeDef

### AllowedOrigins
- **Type**: typing.List[str]
- **Required**: Yes

### AllowedHeaders
- **Type**: typing.List[str]
- **Required**: Yes

### AllowedMethods
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'PUT']]]

### MaxAgeSeconds
- **Type**: typing.Optional[int]

### ExposeHeaders
- **Type**: typing.Optional[typing.List[str]]


# CreateContainerInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediastore_classes.TagTypeDef]]


# CreateContainerOutputTypeDef

### Container
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ContainerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteContainerInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCorsPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLifecyclePolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContainerInputRequestTypeDef

### ContainerName
- **Type**: typing.Optional[str]


# DescribeContainerOutputTypeDef

### Container
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ContainerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerPolicyOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCorsPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCorsPolicyOutputTypeDef

### CorsPolicy
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_classes.CorsRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecyclePolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecyclePolicyOutputTypeDef

### LifecyclePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetricPolicyOutputTypeDef

### MetricPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContainersInputListContainersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediastore_classes.PaginatorConfigTypeDef]


# ListContainersInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContainersOutputTypeDef

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_classes.ContainerTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricPolicyRuleTypeDef

### ObjectGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# MetricPolicyTypeDef

### ContainerLevelMetrics
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MetricPolicyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyRuleTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutContainerPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutCorsPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### CorsPolicy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediastore_classes.CorsRuleTypeDef]
- **Required**: Yes


# PutLifecyclePolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecyclePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutMetricPolicyInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyTypeDef'>
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


# StartAccessLoggingInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopAccessLoggingInputRequestTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediastore_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# UntagResourceInputRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


