# Iotfleethub Classes

# ApplicationSummary

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### applicationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### applicationDescription
- **Type**: typing.Optional[str]

### applicationCreationDate
- **Type**: typing.Optional[int]

### applicationLastUpdateDate
- **Type**: typing.Optional[int]

### applicationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequest

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### applicationDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationResponse

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleethub_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DescribeApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationResponse

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### applicationDescription
- **Type**: <class 'str'>
- **Required**: Yes

### applicationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### applicationState
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### applicationCreationDate
- **Type**: <class 'int'>
- **Required**: Yes

### applicationLastUpdateDate
- **Type**: <class 'int'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ssoClientId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleethub_classes.ResponseMetadata'>
- **Required**: Yes


# ListApplicationsRequest

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotfleethub_classes.PaginatorConfig]


# ListApplicationsResponse

### applicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotfleethub_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleethub_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotfleethub_classes.ResponseMetadata'>
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


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### applicationName
- **Type**: typing.Optional[str]

### applicationDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


