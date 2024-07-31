from datetime import datetime
from pydantic import BaseModel
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

class ParameterValueTypeDef(BaseModel):
    id: str
    stringValue: str

class TagTypeDef(BaseModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeactivatePipelineInputRequestTypeDef(BaseModel):
    pipelineId: str
    cancelActive: Optional[bool] = None

class DeletePipelineInputRequestTypeDef(BaseModel):
    pipelineId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeObjectsInputRequestTypeDef(BaseModel):
    pipelineId: str
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    marker: Optional[str] = None

class DescribePipelinesInputRequestTypeDef(BaseModel):
    pipelineIds: Sequence[str]

class EvaluateExpressionInputRequestTypeDef(BaseModel):
    pipelineId: str
    objectId: str
    expression: str

class FieldTypeDef(BaseModel):
    key: str
    stringValue: Optional[str] = None
    refValue: Optional[str] = None

class GetPipelineDefinitionInputRequestTypeDef(BaseModel):
    pipelineId: str
    version: Optional[str] = None

class InstanceIdentityTypeDef(BaseModel):
    document: Optional[str] = None
    signature: Optional[str] = None

class ListPipelinesInputRequestTypeDef(BaseModel):
    marker: Optional[str] = None

class PipelineIdNameTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class OperatorTypeDef(BaseModel):
    type: Optional[OperatorTypeType] = None
    values: Optional[Sequence[str]] = None

class ParameterAttributeTypeDef(BaseModel):
    key: str
    stringValue: str

class ValidationErrorTypeDef(BaseModel):
    id: Optional[str] = None
    errors: Optional[List[str]] = None

class ValidationWarningTypeDef(BaseModel):
    id: Optional[str] = None
    warnings: Optional[List[str]] = None

class RemoveTagsInputRequestTypeDef(BaseModel):
    pipelineId: str
    tagKeys: Sequence[str]

class ReportTaskRunnerHeartbeatInputRequestTypeDef(BaseModel):
    taskrunnerId: str
    workerGroup: Optional[str] = None
    hostname: Optional[str] = None

class SetStatusInputRequestTypeDef(BaseModel):
    pipelineId: str
    objectIds: Sequence[str]
    status: str

class SetTaskStatusInputRequestTypeDef(BaseModel):
    taskId: str
    taskStatus: TaskStatusType
    errorId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorStackTrace: Optional[str] = None

class ActivatePipelineInputRequestTypeDef(BaseModel):
    pipelineId: str
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None
    startTimestamp: Optional[TimestampTypeDef] = None

class AddTagsInputRequestTypeDef(BaseModel):
    pipelineId: str
    tags: Sequence[TagTypeDef]

class CreatePipelineInputRequestTypeDef(BaseModel):
    name: str
    uniqueId: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreatePipelineOutputTypeDef(BaseModel):
    pipelineId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluateExpressionOutputTypeDef(BaseModel):
    evaluatedExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class QueryObjectsOutputTypeDef(BaseModel):
    ids: List[str]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReportTaskProgressOutputTypeDef(BaseModel):
    canceled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReportTaskRunnerHeartbeatOutputTypeDef(BaseModel):
    terminate: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeObjectsInputDescribeObjectsPaginateTypeDef(BaseModel):
    pipelineId: str
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesInputListPipelinesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PipelineDescriptionTypeDef(BaseModel):
    pipelineId: str
    name: str
    fields: List[FieldTypeDef]
    description: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class PipelineObjectTypeDef(BaseModel):
    id: str
    name: str
    fields: List[FieldTypeDef]

class ReportTaskProgressInputRequestTypeDef(BaseModel):
    taskId: str
    fields: Optional[Sequence[FieldTypeDef]] = None

class PollForTaskInputRequestTypeDef(BaseModel):
    workerGroup: str
    hostname: Optional[str] = None
    instanceIdentity: Optional[InstanceIdentityTypeDef] = None

class ListPipelinesOutputTypeDef(BaseModel):
    pipelineIdList: List[PipelineIdNameTypeDef]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SelectorTypeDef(BaseModel):
    fieldName: Optional[str] = None
    operator: Optional[OperatorTypeDef] = None

class ParameterObjectTypeDef(BaseModel):
    id: str
    attributes: List[ParameterAttributeTypeDef]

class PutPipelineDefinitionOutputTypeDef(BaseModel):
    validationErrors: List[ValidationErrorTypeDef]
    validationWarnings: List[ValidationWarningTypeDef]
    errored: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ValidatePipelineDefinitionOutputTypeDef(BaseModel):
    validationErrors: List[ValidationErrorTypeDef]
    validationWarnings: List[ValidationWarningTypeDef]
    errored: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePipelinesOutputTypeDef(BaseModel):
    pipelineDescriptionList: List[PipelineDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeObjectsOutputTypeDef(BaseModel):
    pipelineObjects: List[PipelineObjectTypeDef]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef

class TaskObjectTypeDef(BaseModel):
    taskId: Optional[str] = None
    pipelineId: Optional[str] = None
    attemptId: Optional[str] = None
    objects: Optional[Dict[str, PipelineObjectTypeDef]] = None

class QueryTypeDef(BaseModel):
    selectors: Optional[Sequence[SelectorTypeDef]] = None

class GetPipelineDefinitionOutputTypeDef(BaseModel):
    pipelineObjects: List[PipelineObjectTypeDef]
    parameterObjects: List[ParameterObjectTypeDef]
    parameterValues: List[ParameterValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPipelineDefinitionInputRequestTypeDef(BaseModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectTypeDef]
    parameterObjects: Optional[Sequence[ParameterObjectTypeDef]] = None
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None

class ValidatePipelineDefinitionInputRequestTypeDef(BaseModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectTypeDef]
    parameterObjects: Optional[Sequence[ParameterObjectTypeDef]] = None
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None

class PollForTaskOutputTypeDef(BaseModel):
    taskObject: TaskObjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryObjectsInputQueryObjectsPaginateTypeDef(BaseModel):
    pipelineId: str
    sphere: str
    query: Optional[QueryTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryObjectsInputRequestTypeDef(BaseModel):
    pipelineId: str
    sphere: str
    query: Optional[QueryTypeDef] = None
    marker: Optional[str] = None
    limit: Optional[int] = None

