# Cloudcontrol Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelResourceRequestInput

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# CancelResourceRequestOutput

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ProgressEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceInput

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


# CreateResourceOutput

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ProgressEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourceInput

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


# DeleteResourceOutput

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ProgressEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceInput

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


# GetResourceOutput

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResourceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceRequestStatusInput

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceRequestStatusInputWait

### RequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetResourceRequestStatusOutput

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ProgressEvent'>
- **Required**: Yes

### HooksProgressEvent
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.HookProgressEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes


# HookProgressEvent

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


# ListResourceRequestsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceRequestStatusFilter
- **Type**: <class 'NoneType'>


# ListResourceRequestsInputPaginate

### ResourceRequestStatusFilter
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.PaginatorConfig]


# ListResourceRequestsOutput

### ResourceRequestStatusSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ProgressEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesInput

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


# ListResourcesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.PaginatorConfig]


# ListResourcesOutput

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResourceDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
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


# ProgressEvent

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


# ResourceDescription

### Identifier
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[str]


# ResourceRequestStatusFilter

### Operations
- **Type**: typing.Optional[typing.List[typing.Literal['CREATE', 'DELETE', 'UPDATE']]]

### OperationStatuses
- **Type**: typing.Optional[typing.List[typing.Literal['CANCEL_COMPLETE', 'CANCEL_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCESS']]]


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


# UpdateResourceInput

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


# UpdateResourceOutput

### ProgressEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ProgressEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


