# Mediastore Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Container

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


# CorsRule

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


# CorsRuleOutput

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


# CreateContainerInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.Tag]]


# CreateContainerOutput

### Container
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.Container'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteContainerInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCorsPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLifecyclePolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContainerInput

### ContainerName
- **Type**: typing.Optional[str]


# DescribeContainerOutput

### Container
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.Container'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerPolicyOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# GetCorsPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCorsPolicyOutput

### CorsPolicy
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.CorsRuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# GetLifecyclePolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLifecyclePolicyOutput

### LifecyclePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetricPolicyOutput

### MetricPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.MetricPolicyOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# ListContainersInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContainersInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.PaginatorConfig]


# ListContainersOutput

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.Container]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediastore.mediastore_classes.ResponseMetadata'>
- **Required**: Yes


# MetricPolicy

### ContainerLevelMetrics
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MetricPolicyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.MetricPolicyRule]]


# MetricPolicyOutput

### ContainerLevelMetrics
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MetricPolicyRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.MetricPolicyRule]]


# MetricPolicyRule

### ObjectGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutContainerPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutCorsPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### CorsPolicy
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.CorsRule, aws_resource_validator.pydantic_models.mediastore.mediastore_classes.CorsRuleOutput]]
- **Required**: Yes


# PutLifecyclePolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### LifecyclePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutMetricPolicyInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.MetricPolicy, aws_resource_validator.pydantic_models.mediastore.mediastore_classes.MetricPolicyOutput]
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


# StartAccessLoggingInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopAccessLoggingInput

### ContainerName
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceInput

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediastore.mediastore_classes.Tag]
- **Required**: Yes


# UntagResourceInput

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


