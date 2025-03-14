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


# CorsRuleOutputTypeDef

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


# CorsRuleTypeDef

### AllowedOrigins
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllowedHeaders
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllowedMethods
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE', 'GET', 'HEAD', 'PUT']]]

### MaxAgeSeconds
- **Type**: typing.Optional[int]

### ExposeHeaders
- **Type**: typing.Optional[typing.Sequence[str]]


# CorsRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateContainerInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediastore_classes.TagTypeDef]]


# DeleteContainerInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCorsPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLifecyclePolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContainerInputTypeDef

### ContainerName
- **Type**: typing.Optional[str]


# GetContainerPolicyInputTypeDef

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


# GetCorsPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCorsPolicyOutputTypeDef

### CorsPolicy
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_classes.CorsRuleOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecyclePolicyInputTypeDef

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


# GetMetricPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetricPolicyOutputTypeDef

### MetricPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContainersInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediastore_classes.PaginatorConfigTypeDef]


# ListContainersInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContainersOutputTypeDef

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore_classes.ContainerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

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


# MetricPolicyOutputTypeDef

### ContainerLevelMetrics
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MetricPolicyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyRuleTypeDef]]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyRuleTypeDef]]


# MetricPolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutContainerPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutCorsPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### CorsPolicy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediastore_classes.CorsRuleUnionTypeDef]
- **Required**: Yes


# PutLifecyclePolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecyclePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutMetricPolicyInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore_classes.MetricPolicyUnionTypeDef'>
- **Required**: Yes


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


# StartAccessLoggingInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopAccessLoggingInputTypeDef

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputTypeDef

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


# UntagResourceInputTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


