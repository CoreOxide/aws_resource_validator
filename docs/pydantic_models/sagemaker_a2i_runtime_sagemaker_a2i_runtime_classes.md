# Sagemaker A2I Runtime Sagemaker A2I Runtime Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteHumanLoopRequest

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHumanLoopRequest

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHumanLoopResponse

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### FailureCode
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.HumanLoopOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# HumanLoopDataAttributes

### ContentClassifiers
- **Type**: typing.List[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]
- **Required**: Yes


# HumanLoopInput

### InputContent
- **Type**: <class 'str'>
- **Required**: Yes


# HumanLoopOutput

### OutputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# HumanLoopSummary

### HumanLoopName
- **Type**: typing.Optional[str]

### HumanLoopStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### FlowDefinitionArn
- **Type**: typing.Optional[str]


# ListHumanLoopsRequest

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHumanLoopsRequestPaginate

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.PaginatorConfig]


# ListHumanLoopsResponse

### HumanLoopSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.HumanLoopSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.ResponseMetadata'>
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


# StartHumanLoopRequest

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.HumanLoopInput'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.HumanLoopDataAttributes]


# StartHumanLoopResponse

### HumanLoopArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime.sagemaker_a2i_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# StopHumanLoopRequest

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes


