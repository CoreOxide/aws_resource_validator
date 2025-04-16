from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.datapipeline_constants import *

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
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    marker: Optional[str] = None


class DescribePipelinesInput(BaseValidatorModel):
    pipelineIds: Sequence[str]


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


class ParameterAttribute(BaseValidatorModel):
    key: str
    stringValue: str


class RemoveTagsInput(BaseValidatorModel):
    pipelineId: str
    tagKeys: Sequence[str]


class ReportTaskRunnerHeartbeatInput(BaseValidatorModel):
    taskrunnerId: str
    workerGroup: Optional[str] = None
    hostname: Optional[str] = None


class SetStatusInput(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    status: str


class SetTaskStatusInput(BaseValidatorModel):
    taskId: str
    taskStatus: TaskStatusType
    errorId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorStackTrace: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class ParameterValue(BaseValidatorModel):
    pass


class ActivatePipelineInput(BaseValidatorModel):
    pipelineId: str
    parameterValues: Optional[Sequence[ParameterValue]] = None
    startTimestamp: Optional[Timestamp] = None


class AddTagsInput(BaseValidatorModel):
    pipelineId: str
    tags: Sequence[Tag]


class CreatePipelineInput(BaseValidatorModel):
    name: str
    uniqueId: str
    description: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


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
    objectIds: Sequence[str]
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


class ReportTaskProgressInput(BaseValidatorModel):
    taskId: str
    fields: Optional[Sequence[Field]] = None


class PollForTaskInput(BaseValidatorModel):
    workerGroup: str
    hostname: Optional[str] = None
    instanceIdentity: Optional[InstanceIdentity] = None


class PipelineIdName(BaseValidatorModel):
    pass


class ListPipelinesOutput(BaseValidatorModel):
    pipelineIdList: List[PipelineIdName]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadata


class ValidationWarning(BaseValidatorModel):
    pass


class ValidationError(BaseValidatorModel):
    pass


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


class PipelineObjectOutput(BaseValidatorModel):
    pass


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


class Selector(BaseValidatorModel):
    pass


class Query(BaseValidatorModel):
    selectors: Optional[Sequence[Selector]] = None


class ParameterObjectOutput(BaseValidatorModel):
    pass


class GetPipelineDefinitionOutput(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectOutput]
    parameterObjects: List[ParameterObjectOutput]
    parameterValues: List[ParameterValue]
    ResponseMetadata: ResponseMetadata


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


class PipelineObjectUnion(BaseValidatorModel):
    pass


class ParameterObjectUnion(BaseValidatorModel):
    pass


class PutPipelineDefinitionInput(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectUnion]
    parameterObjects: Optional[Sequence[ParameterObjectUnion]] = None
    parameterValues: Optional[Sequence[ParameterValue]] = None


class ValidatePipelineDefinitionInput(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectUnion]
    parameterObjects: Optional[Sequence[ParameterObjectUnion]] = None
    parameterValues: Optional[Sequence[ParameterValue]] = None


