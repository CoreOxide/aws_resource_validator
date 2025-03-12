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

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeactivatePipelineInputTypeDef(BaseValidatorModel):
    pipelineId: str
    cancelActive: Optional[bool] = None


class DeletePipelineInputTypeDef(BaseValidatorModel):
    pipelineId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeObjectsInputTypeDef(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    marker: Optional[str] = None


class DescribePipelinesInputTypeDef(BaseValidatorModel):
    pipelineIds: Sequence[str]


class EvaluateExpressionInputTypeDef(BaseValidatorModel):
    pipelineId: str
    objectId: str
    expression: str


class FieldTypeDef(BaseValidatorModel):
    key: str
    stringValue: Optional[str] = None
    refValue: Optional[str] = None


class GetPipelineDefinitionInputTypeDef(BaseValidatorModel):
    pipelineId: str
    version: Optional[str] = None


class InstanceIdentityTypeDef(BaseValidatorModel):
    document: Optional[str] = None
    signature: Optional[str] = None


class ListPipelinesInputTypeDef(BaseValidatorModel):
    marker: Optional[str] = None


class ParameterAttributeTypeDef(BaseValidatorModel):
    key: str
    stringValue: str


class RemoveTagsInputTypeDef(BaseValidatorModel):
    pipelineId: str
    tagKeys: Sequence[str]


class ReportTaskRunnerHeartbeatInputTypeDef(BaseValidatorModel):
    taskrunnerId: str
    workerGroup: Optional[str] = None
    hostname: Optional[str] = None


class SetStatusInputTypeDef(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    status: str


class SetTaskStatusInputTypeDef(BaseValidatorModel):
    taskId: str
    taskStatus: TaskStatusType
    errorId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorStackTrace: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ParameterValueTypeDef(BaseValidatorModel):
    pass


class ActivatePipelineInputTypeDef(BaseValidatorModel):
    pipelineId: str
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None
    startTimestamp: Optional[TimestampTypeDef] = None


class AddTagsInputTypeDef(BaseValidatorModel):
    pipelineId: str
    tags: Sequence[TagTypeDef]


class CreatePipelineInputTypeDef(BaseValidatorModel):
    name: str
    uniqueId: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreatePipelineOutputTypeDef(BaseValidatorModel):
    pipelineId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluateExpressionOutputTypeDef(BaseValidatorModel):
    evaluatedExpression: str
    ResponseMetadata: ResponseMetadataTypeDef


class QueryObjectsOutputTypeDef(BaseValidatorModel):
    ids: List[str]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ReportTaskProgressOutputTypeDef(BaseValidatorModel):
    canceled: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ReportTaskRunnerHeartbeatOutputTypeDef(BaseValidatorModel):
    terminate: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeObjectsInputPaginateTypeDef(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPipelinesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PipelineDescriptionTypeDef(BaseValidatorModel):
    pipelineId: str
    name: str
    fields: List[FieldTypeDef]
    description: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None


class ReportTaskProgressInputTypeDef(BaseValidatorModel):
    taskId: str
    fields: Optional[Sequence[FieldTypeDef]] = None


class PollForTaskInputTypeDef(BaseValidatorModel):
    workerGroup: str
    hostname: Optional[str] = None
    instanceIdentity: Optional[InstanceIdentityTypeDef] = None


class PipelineIdNameTypeDef(BaseValidatorModel):
    pass


class ListPipelinesOutputTypeDef(BaseValidatorModel):
    pipelineIdList: List[PipelineIdNameTypeDef]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ValidationWarningTypeDef(BaseValidatorModel):
    pass


class ValidationErrorTypeDef(BaseValidatorModel):
    pass


class PutPipelineDefinitionOutputTypeDef(BaseValidatorModel):
    validationErrors: List[ValidationErrorTypeDef]
    validationWarnings: List[ValidationWarningTypeDef]
    errored: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ValidatePipelineDefinitionOutputTypeDef(BaseValidatorModel):
    validationErrors: List[ValidationErrorTypeDef]
    validationWarnings: List[ValidationWarningTypeDef]
    errored: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePipelinesOutputTypeDef(BaseValidatorModel):
    pipelineDescriptionList: List[PipelineDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PipelineObjectOutputTypeDef(BaseValidatorModel):
    pass


class DescribeObjectsOutputTypeDef(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectOutputTypeDef]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef


class TaskObjectTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    pipelineId: Optional[str] = None
    attemptId: Optional[str] = None
    objects: Optional[Dict[str, PipelineObjectOutputTypeDef]] = None


class SelectorTypeDef(BaseValidatorModel):
    pass


class QueryTypeDef(BaseValidatorModel):
    selectors: Optional[Sequence[SelectorTypeDef]] = None


class ParameterObjectOutputTypeDef(BaseValidatorModel):
    pass


class GetPipelineDefinitionOutputTypeDef(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectOutputTypeDef]
    parameterObjects: List[ParameterObjectOutputTypeDef]
    parameterValues: List[ParameterValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PollForTaskOutputTypeDef(BaseValidatorModel):
    taskObject: TaskObjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class QueryObjectsInputPaginateTypeDef(BaseValidatorModel):
    pipelineId: str
    sphere: str
    query: Optional[QueryTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class QueryObjectsInputTypeDef(BaseValidatorModel):
    pipelineId: str
    sphere: str
    query: Optional[QueryTypeDef] = None
    marker: Optional[str] = None
    limit: Optional[int] = None


class PipelineObjectUnionTypeDef(BaseValidatorModel):
    pass


class ParameterObjectUnionTypeDef(BaseValidatorModel):
    pass


class PutPipelineDefinitionInputTypeDef(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectUnionTypeDef]
    parameterObjects: Optional[Sequence[ParameterObjectUnionTypeDef]] = None
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None


class ValidatePipelineDefinitionInputTypeDef(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectUnionTypeDef]
    parameterObjects: Optional[Sequence[ParameterObjectUnionTypeDef]] = None
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None


