# Pydantic Models in datapipeline_classes

# ActivatePipelineInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### parameterValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterValueTypeDef]]

### startTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# AddTagsInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.TagTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePipelineInputRequestTypeDef

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


# DeactivatePipelineInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### cancelActive
- **Type**: typing.Optional[bool]


# DeletePipelineInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeObjectsInputDescribeObjectsPaginateTypeDef

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


# DescribeObjectsInputRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectTypeDef]
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


# DescribePipelinesInputRequestTypeDef

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


# EvaluateExpressionInputRequestTypeDef

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


# GetPipelineDefinitionInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]


# GetPipelineDefinitionOutputTypeDef

### pipelineObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectTypeDef]
- **Required**: Yes

### parameterObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectTypeDef]
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


# ListPipelinesInputListPipelinesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.PaginatorConfigTypeDef]


# ListPipelinesInputRequestTypeDef

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


# OperatorTypeDef

### type
- **Type**: typing.Optional[typing.Literal['BETWEEN', 'EQ', 'GE', 'LE', 'REF_EQ']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


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


# ParameterObjectTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterAttributeTypeDef]
- **Required**: Yes


# ParameterValueTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stringValue
- **Type**: <class 'str'>
- **Required**: Yes


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

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# PipelineObjectTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.datapipeline_classes.FieldTypeDef]
- **Required**: Yes


# PollForTaskInputRequestTypeDef

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


# PutPipelineDefinitionInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectTypeDef]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectTypeDef]]

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


# QueryObjectsInputQueryObjectsPaginateTypeDef

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


# QueryObjectsInputRequestTypeDef

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


# RemoveTagsInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReportTaskProgressInputRequestTypeDef

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


# ReportTaskRunnerHeartbeatInputRequestTypeDef

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


# SelectorTypeDef

### fieldName
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datapipeline_classes.OperatorTypeDef]


# SetStatusInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### objectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes


# SetTaskStatusInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectTypeDef]]


# ValidatePipelineDefinitionInputRequestTypeDef

### pipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineObjects
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.PipelineObjectTypeDef]
- **Required**: Yes

### parameterObjects
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datapipeline_classes.ParameterObjectTypeDef]]

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

### id
- **Type**: typing.Optional[str]

### errors
- **Type**: typing.Optional[typing.List[str]]


# ValidationWarningTypeDef

### id
- **Type**: typing.Optional[str]

### warnings
- **Type**: typing.Optional[typing.List[str]]


