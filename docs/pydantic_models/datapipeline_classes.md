# Datapipeline Classes

# ActivatePipelineInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValueTypeDef]]

### startTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.TimestampTypeDef]


# AddTagsInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.TagTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePipelineInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### uniqueId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.TagTypeDef]]


# CreatePipelineOutputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeactivatePipelineInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### cancelActive
- **Type**: typing.Optional[bool]


# DeletePipelineInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectsInputPaginateTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### evaluateExpressions
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfigTypeDef]


# DescribeObjectsInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### evaluateExpressions
- **Type**: typing.Optional[bool]

### marker
- **Type**: typing.Optional[str]


# DescribeObjectsOutputTypeDef

### pipelineObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectOutputTypeDef]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePipelinesInputTypeDef

### pipelineIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribePipelinesOutputTypeDef

### pipelineDescriptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluateExpressionInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectId
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateExpressionOutputTypeDef

### evaluatedExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FieldTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: typing.Optional[str]

### refValue
- **Type**: typing.Optional[str]


# GetPipelineDefinitionInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]


# GetPipelineDefinitionOutputTypeDef

### pipelineObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectOutputTypeDef]
- **Required**: Yes

### parameterObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectOutputTypeDef]
- **Required**: Yes

### parameterValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValueTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceIdentityTypeDef

### document
- **Type**: typing.Optional[str]

### signature
- **Type**: typing.Optional[str]


# ListPipelinesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfigTypeDef]


# ListPipelinesInputTypeDef

### marker
- **Type**: typing.Optional[str]


# ListPipelinesOutputTypeDef

### pipelineIdList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineIdNameTypeDef]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterAttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: <class 'str'>
- **Required**: Yes


# ParameterObjectOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterObjectUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterValueTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineDescriptionTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.FieldTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.TagTypeDef]]


# PipelineIdNameTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineObjectOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineObjectUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PollForTaskInputTypeDef

### workerGroup
- **Type**: <class 'str'>
- **Required**: Yes

### hostname
- **Type**: typing.Optional[str]

### instanceIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.InstanceIdentityTypeDef]


# PollForTaskOutputTypeDef

### taskObject
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.TaskObjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPipelineDefinitionInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectUnionTypeDef]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectUnionTypeDef]]

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValueTypeDef]]


# PutPipelineDefinitionOutputTypeDef

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationErrorTypeDef]
- **Required**: Yes

### validationWarnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationWarningTypeDef]
- **Required**: Yes

### errored
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryObjectsInputPaginateTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### sphere
- **Type**: <class 'str'>
- **Required**: Yes

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.QueryTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfigTypeDef]


# QueryObjectsInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### sphere
- **Type**: <class 'str'>
- **Required**: Yes

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.QueryTypeDef]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# QueryObjectsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryTypeDef

### selectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.SelectorTypeDef]]


# RemoveTagsInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReportTaskProgressInputTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.FieldTypeDef]]


# ReportTaskProgressOutputTypeDef

### canceled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReportTaskRunnerHeartbeatInputTypeDef

### taskrunnerId
- **Type**: <class 'str'>
- **Required**: Yes

### workerGroup
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]


# ReportTaskRunnerHeartbeatOutputTypeDef

### terminate
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
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


# SelectorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetStatusInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes


# SetTaskStatusInputTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### taskStatus
- **Type**: typing.Literal['FAILED', 'FALSE', 'FINISHED']
- **Required**: Yes

### errorId
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorStackTrace
- **Type**: typing.Optional[str]


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TaskObjectTypeDef

### taskId
- **Type**: typing.Optional[str]

### pipelineId
- **Type**: typing.Optional[str]

### attemptId
- **Type**: typing.Optional[str]

### objects
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectOutputTypeDef]]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValidatePipelineDefinitionInputTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectUnionTypeDef]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectUnionTypeDef]]

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValueTypeDef]]


# ValidatePipelineDefinitionOutputTypeDef

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationErrorTypeDef]
- **Required**: Yes

### validationWarnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationWarningTypeDef]
- **Required**: Yes

### errored
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidationErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValidationWarningTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

