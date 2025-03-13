# Cloudcontrol Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelResourceRequestInputTypeDef

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


# CreateResourceInputTypeDef

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


# DeleteResourceInputTypeDef

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


# GetResourceInputTypeDef

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


# GetResourceRequestStatusInputTypeDef

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceRequestStatusInputWaitTypeDef

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.WaiterConfigTypeDef]


# GetResourceRequestStatusOutputTypeDef

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ProgressEventTypeDef'>
- **Required**: Yes

### HooksProgressEvent
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudcontrol_classes.HookProgressEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HookProgressEventTypeDef

### HookTypeName
- **Type**: typing.Optional[str]

### HookTypeVersionId
- **Type**: typing.Optional[str]

### HookTypeArn
- **Type**: typing.Optional[str]

### InvocationPoint
- **Type**: typing.Optional[str]

### HookStatus
- **Type**: typing.Optional[str]

### HookEventTime
- **Type**: typing.Optional[datetime.datetime]

### HookStatusMessage
- **Type**: typing.Optional[str]

### FailureMode
- **Type**: typing.Optional[str]


# ListResourceRequestsInputPaginateTypeDef

### ResourceRequestStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.ResourceRequestStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol_classes.PaginatorConfigTypeDef]


# ListResourceRequestsInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesInputPaginateTypeDef

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


# ListResourcesInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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

### HooksRequestToken
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
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AlreadyExists', 'GeneralServiceException', 'InternalFailure', 'InvalidCredentials', 'InvalidRequest', 'NetworkFailure', 'NotFound', 'NotStabilized', 'NotUpdatable', 'ResourceConflict', 'ServiceInternalError', 'ServiceLimitExceeded', 'ServiceTimeout', 'Throttling', 'UnauthorizedTaggingOperation']]

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


# UpdateResourceInputTypeDef

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


