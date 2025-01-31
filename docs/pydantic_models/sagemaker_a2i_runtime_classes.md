# sagemaker_a2i_runtime_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteHumanLoopRequestRequestTypeDef

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHumanLoopRequestRequestTypeDef

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHumanLoopResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.HumanLoopOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HumanLoopDataAttributesTypeDef

### ContentClassifiers
- **Type**: typing.Sequence[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]
- **Required**: Yes


# HumanLoopInputTypeDef

### InputContent
- **Type**: <class 'str'>
- **Required**: Yes


# HumanLoopOutputTypeDef

### OutputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# HumanLoopSummaryTypeDef

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


# ListHumanLoopsRequestListHumanLoopsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.PaginatorConfigTypeDef]


# ListHumanLoopsRequestRequestTypeDef

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


# ListHumanLoopsResponseTypeDef

### HumanLoopSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.HumanLoopSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.ResponseMetadataTypeDef'>
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


# StartHumanLoopRequestRequestTypeDef

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.HumanLoopInputTypeDef'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.HumanLoopDataAttributesTypeDef]


# StartHumanLoopResponseTypeDef

### HumanLoopArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_a2i_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopHumanLoopRequestRequestTypeDef

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes


