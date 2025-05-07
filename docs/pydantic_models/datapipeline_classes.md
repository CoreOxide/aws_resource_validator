# Datapipeline Classes

# ActivatePipelineInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### parameterValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterValue]]

### startTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# AddTagsInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Tag]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Tag]]


# CreatePipelineOutput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
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
- **Type**: typing.List[str]
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
- **Type**: typing.List[str]
- **Required**: Yes

### evaluateExpressions
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PaginatorConfig]


# DescribeObjectsOutput

### pipelineObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObjectOutput]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipelinesInput

### pipelineIds
- **Type**: typing.List[str]
- **Required**: Yes


# DescribePipelinesOutput

### pipelineDescriptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObjectOutput]
- **Required**: Yes

### parameterObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterObjectOutput]
- **Required**: Yes

### parameterValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PaginatorConfig]


# ListPipelinesOutput

### pipelineIdList
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineIdName]
- **Required**: Yes

### marker
- **Type**: <class 'str'>
- **Required**: Yes

### hasMoreResults
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# Operator

### type
- **Type**: typing.Optional[typing.Literal['BETWEEN', 'EQ', 'GE', 'LE', 'REF_EQ']]

### values
- **Type**: typing.Optional[typing.List[str]]


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


# ParameterObject

### id
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterAttribute]
- **Required**: Yes


# ParameterObjectOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterAttribute]
- **Required**: Yes


# ParameterValue

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: <class 'str'>
- **Required**: Yes


# PipelineDescription

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Field]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Tag]]


# PipelineIdName

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# PipelineObject

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Field]
- **Required**: Yes


# PipelineObjectOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Field]
- **Required**: Yes


# PollForTaskInput

### workerGroup
- **Type**: <class 'str'>
- **Required**: Yes

### hostname
- **Type**: typing.Optional[str]

### instanceIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.InstanceIdentity]


# PollForTaskOutput

### taskObject
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.TaskObject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PutPipelineDefinitionInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObject, aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObjectOutput]]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterObject, aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterObjectOutput]]]

### parameterValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterValue]]


# PutPipelineDefinitionOutput

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ValidationError]
- **Required**: Yes

### validationWarnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ValidationWarning]
- **Required**: Yes

### errored
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# Query

### selectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Selector]]


# QueryObjectsInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### sphere
- **Type**: <class 'str'>
- **Required**: Yes

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Query]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Query]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PaginatorConfig]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# ReportTaskProgressInput

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Field]]


# ReportTaskProgressOutput

### canceled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
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

### fieldName
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.Operator]


# SetStatusInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.List[str]
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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObjectOutput]]


# ValidatePipelineDefinitionInput

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObject, aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.PipelineObjectOutput]]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterObject, aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterObjectOutput]]]

### parameterValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ParameterValue]]


# ValidatePipelineDefinitionOutput

### validationErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ValidationError]
- **Required**: Yes

### validationWarnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ValidationWarning]
- **Required**: Yes

### errored
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datapipeline.datapipeline_classes.ResponseMetadata'>
- **Required**: Yes


# ValidationError

### id
- **Type**: typing.Optional[str]

### errors
- **Type**: typing.Optional[typing.List[str]]


# ValidationWarning

### id
- **Type**: typing.Optional[str]

### warnings
- **Type**: typing.Optional[typing.List[str]]


