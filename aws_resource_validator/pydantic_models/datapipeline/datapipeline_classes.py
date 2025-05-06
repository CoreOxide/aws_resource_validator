from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.datapipeline.datapipeline_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ParameterValue(BaseValidatorModel):
    id: str
    stringValue: str

Timestamp = Union[datetime, str]


class Tag(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeactivatePipelineInput(BaseValidatorModel):
    pipelineId: str
    cancelActive: Optional[bool] = None


class DeletePipelineInput(BaseValidatorModel):
    pipelineId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeObjectsInput(BaseValidatorModel):
    pipelineId: str
    objectIds: List[str]
    evaluateExpressions: Optional[bool] = None
    marker: Optional[str] = None


class DescribePipelinesInput(BaseValidatorModel):
    pipelineIds: List[str]


class EvaluateExpressionInput(BaseValidatorModel):
    pipelineId: str
    objectId: str
    expression: str


class Field(BaseValidatorModel):
    key: str
    stringValue: Optional[str] = None
    refValue: Optional[str] = None


class GetPipelineDefinitionInput(BaseValidatorModel):
    pipelineId: str
    version: Optional[str] = None


class InstanceIdentity(BaseValidatorModel):
    document: Optional[str] = None
    signature: Optional[str] = None


class ListPipelinesInput(BaseValidatorModel):
    marker: Optional[str] = None


class PipelineIdName(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class Operator(BaseValidatorModel):
    type: Optional[OperatorTypeType] = None
    values: Optional[List[str]] = None


class ParameterAttribute(BaseValidatorModel):
    key: str
    stringValue: str


class ValidationError(BaseValidatorModel):
    id: Optional[str] = None
    errors: Optional[List[str]] = None


class ValidationWarning(BaseValidatorModel):
    id: Optional[str] = None
    warnings: Optional[List[str]] = None


class RemoveTagsInput(BaseValidatorModel):
    pipelineId: str
    tagKeys: List[str]


class ReportTaskRunnerHeartbeatInput(BaseValidatorModel):
    taskrunnerId: str
    workerGroup: Optional[str] = None
    hostname: Optional[str] = None


class SetStatusInput(BaseValidatorModel):
    pipelineId: str
    objectIds: List[str]
    status: str


class SetTaskStatusInput(BaseValidatorModel):
    taskId: str
    taskStatus: TaskStatusType
    errorId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorStackTrace: Optional[str] = None


class ActivatePipelineInput(BaseValidatorModel):
    pipelineId: str
    parameterValues: Optional[List[ParameterValue]] = None
    startTimestamp: Optional[Timestamp] = None


class AddTagsInput(BaseValidatorModel):
    pipelineId: str
    tags: List[Tag]


class CreatePipelineInput(BaseValidatorModel):
    name: str
    uniqueId: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreatePipelineOutput(BaseValidatorModel):
    pipelineId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EvaluateExpressionOutput(BaseValidatorModel):
    evaluatedExpression: str
    ResponseMetadata: ResponseMetadata


class QueryObjectsOutput(BaseValidatorModel):
    ids: List[str]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadata


class ReportTaskProgressOutput(BaseValidatorModel):
    canceled: bool
    ResponseMetadata: ResponseMetadata


class ReportTaskRunnerHeartbeatOutput(BaseValidatorModel):
    terminate: bool
    ResponseMetadata: ResponseMetadata


class DescribeObjectsInputPaginate(BaseValidatorModel):
    pipelineId: str
    objectIds: List[str]
    evaluateExpressions: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelinesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class PipelineDescription(BaseValidatorModel):
    pipelineId: str
    name: str
    fields: List[Field]
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class PipelineObjectOutput(BaseValidatorModel):
    id: str
    name: str
    fields: List[Field]


class PipelineObject(BaseValidatorModel):
    id: str
    name: str
    fields: List[Field]


class ReportTaskProgressInput(BaseValidatorModel):
    taskId: str
    fields: Optional[List[Field]] = None


class PollForTaskInput(BaseValidatorModel):
    workerGroup: str
    hostname: Optional[str] = None
    instanceIdentity: Optional[InstanceIdentity] = None


class ListPipelinesOutput(BaseValidatorModel):
    pipelineIdList: List[PipelineIdName]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadata


class Selector(BaseValidatorModel):
    fieldName: Optional[str] = None
    operator: Optional[Operator] = None


class ParameterObjectOutput(BaseValidatorModel):
    id: str
    attributes: List[ParameterAttribute]


class ParameterObject(BaseValidatorModel):
    id: str
    attributes: List[ParameterAttribute]


class PutPipelineDefinitionOutput(BaseValidatorModel):
    validationErrors: List[ValidationError]
    validationWarnings: List[ValidationWarning]
    errored: bool
    ResponseMetadata: ResponseMetadata


class ValidatePipelineDefinitionOutput(BaseValidatorModel):
    validationErrors: List[ValidationError]
    validationWarnings: List[ValidationWarning]
    errored: bool
    ResponseMetadata: ResponseMetadata


class DescribePipelinesOutput(BaseValidatorModel):
    pipelineDescriptionList: List[PipelineDescription]
    ResponseMetadata: ResponseMetadata


class DescribeObjectsOutput(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectOutput]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadata


class TaskObject(BaseValidatorModel):
    taskId: Optional[str] = None
    pipelineId: Optional[str] = None
    attemptId: Optional[str] = None
    objects: Optional[Dict[str, PipelineObjectOutput]] = None

PipelineObjectUnion = Union[PipelineObject, PipelineObjectOutput]


class Query(BaseValidatorModel):
    selectors: Optional[List[Selector]] = None


class GetPipelineDefinitionOutput(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectOutput]
    parameterObjects: List[ParameterObjectOutput]
    parameterValues: List[ParameterValue]
    ResponseMetadata: ResponseMetadata

ParameterObjectUnion = Union[ParameterObject, ParameterObjectOutput]


class PollForTaskOutput(BaseValidatorModel):
    taskObject: TaskObject
    ResponseMetadata: ResponseMetadata


class QueryObjectsInputPaginate(BaseValidatorModel):
    pipelineId: str
    sphere: str
    query: Optional[Query] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class QueryObjectsInput(BaseValidatorModel):
    pipelineId: str
    sphere: str
    query: Optional[Query] = None
    marker: Optional[str] = None
    limit: Optional[int] = None


class PutPipelineDefinitionInput(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: List[PipelineObjectUnion]
    parameterObjects: Optional[List[ParameterObjectUnion]] = None
    parameterValues: Optional[List[ParameterValue]] = None


class ValidatePipelineDefinitionInput(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: List[PipelineObjectUnion]
    parameterObjects: Optional[List[ParameterObjectUnion]] = None
    parameterValues: Optional[List[ParameterValue]] = None