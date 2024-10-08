# Pydantic Models in cloudcontrol_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelResourceRequestInputRequestTypeDef

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CancelResourceRequestOutputTypeDef

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceInputRequestTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateResourceOutputTypeDef

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourceInputRequestTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# DeleteResourceOutputTypeDef

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceInputRequestTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# GetResourceOutputTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResourceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceRequestStatusInputRequestTypeDef

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceRequestStatusInputResourceRequestSuccessWaitTypeDef

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.WaiterConfigTypeDef]


# GetResourceRequestStatusOutputTypeDef

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceRequestsInputListResourceRequestsPaginateTypeDef

### ResourceRequestStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.ResourceRequestStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.PaginatorConfigTypeDef]


# ListResourceRequestsInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceRequestStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.ResourceRequestStatusFilterTypeDef]


# ListResourceRequestsOutputTypeDef

### ResourceRequestStatusSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourcesInputListResourcesPaginateTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ResourceModel
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.PaginatorConfigTypeDef]


# ListResourcesInputRequestTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceModel
- **Type**: typing.Optional[str]


# ListResourcesOutputTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudcontrol_classes.ResourceDescriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProgressEventTypeDef

### TypeName
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### RequestToken
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### OperationStatus
- **Type**: typing.Optional[typing.Literal['CANCEL_COMPLETE', 'CANCEL_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceModel
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AlreadyExists', 'GeneralServiceException', 'InternalFailure', 'InvalidCredentials', 'InvalidRequest', 'NetworkFailure', 'NotFound', 'NotStabilized', 'NotUpdatable', 'ResourceConflict', 'ServiceInternalError', 'ServiceLimitExceeded', 'ServiceTimeout', 'Throttling']]

### RetryAfter
- **Type**: typing.Optional[datetime.datetime]


# ResourceDescriptionTypeDef

### Identifier
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[str]


# ResourceRequestStatusFilterTypeDef

### Operations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE', 'DELETE', 'UPDATE']]]

### OperationStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCEL_COMPLETE', 'CANCEL_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']]]


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


# UpdateResourceInputRequestTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PatchDocument
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersionId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# UpdateResourceOutputTypeDef

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


