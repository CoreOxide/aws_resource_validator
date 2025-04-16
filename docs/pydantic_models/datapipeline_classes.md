# Datapipeline Classes

# ActivatePipelineInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValue]]

### startTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.Timestamp]


# AddTagsInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.Tag]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePipelineInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### uniqueId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.Tag]]


# CreatePipelineOutput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# DeactivatePipelineInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### cancelActive
- **Type**: typing.Optional[bool]


# DeletePipelineInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectsInput

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


# DescribeObjectsInputPaginate

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### evaluateExpressions
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfig]


# DescribeObjectsOutput

### pipelineObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectOutput]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipelinesInput

### pipelineIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribePipelinesOutput

### pipelineDescriptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# EvaluateExpressionInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectId
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateExpressionOutput

### evaluatedExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# Field

### key
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: typing.Optional[str]

### refValue
- **Type**: typing.Optional[str]


# GetPipelineDefinitionInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]


# GetPipelineDefinitionOutput

### pipelineObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectOutput]
- **Required**: Yes

### parameterObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectOutput]
- **Required**: Yes

### parameterValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceIdentity

### document
- **Type**: typing.Optional[str]

### signature
- **Type**: typing.Optional[str]


# ListPipelinesInput

### marker
- **Type**: typing.Optional[str]


# ListPipelinesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfig]


# ListPipelinesOutput

### pipelineIdList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineIdName]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterAttribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: <class 'str'>
- **Required**: Yes


# ParameterObjectOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterObjectUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterValue

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineDescription

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.Field]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.Tag]]


# PipelineIdName

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineObjectOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineObjectUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PollForTaskInput

### workerGroup
- **Type**: <class 'str'>
- **Required**: Yes

### hostname
- **Type**: typing.Optional[str]

### instanceIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.InstanceIdentity]


# PollForTaskOutput

### taskObject
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.TaskObject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PutPipelineDefinitionInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectUnion]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectUnion]]

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValue]]


# PutPipelineDefinitionOutput

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationError]
- **Required**: Yes

### validationWarnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationWarning]
- **Required**: Yes

### errored
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# Query

### selectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.Selector]]


# QueryObjectsInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### sphere
- **Type**: <class 'str'>
- **Required**: Yes

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.Query]

### marker
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# QueryObjectsInputPaginate

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### sphere
- **Type**: <class 'str'>
- **Required**: Yes

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.Query]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfig]


# QueryObjectsOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReportTaskProgressInput

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.Field]]


# ReportTaskProgressOutput

### canceled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# ReportTaskRunnerHeartbeatInput

### taskrunnerId
- **Type**: <class 'str'>
- **Required**: Yes

### workerGroup
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]


# ReportTaskRunnerHeartbeatOutput

### terminate
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
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


# Selector

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetStatusInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes


# SetTaskStatusInput

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


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TaskObject

### taskId
- **Type**: typing.Optional[str]

### pipelineId
- **Type**: typing.Optional[str]

### attemptId
- **Type**: typing.Optional[str]

### objects
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectOutput]]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValidatePipelineDefinitionInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectUnion]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectUnion]]

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValue]]


# ValidatePipelineDefinitionOutput

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationError]
- **Required**: Yes

### validationWarnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ValidationWarning]
- **Required**: Yes

### errored
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# ValidationError

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValidationWarning

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

