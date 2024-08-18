from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ParameterValueTypeDef(BaseValidatorModel):
    id: str
    stringValue: str

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeactivatePipelineInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    cancelActive: Optional[bool] = None

class DeletePipelineInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeObjectsInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    marker: Optional[str] = None

class DescribePipelinesInputRequestTypeDef(BaseValidatorModel):
    pipelineIds: Sequence[str]

class EvaluateExpressionInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    objectId: str
    expression: str

class FieldTypeDef(BaseValidatorModel):
    key: str
    stringValue: Optional[str] = None
    refValue: Optional[str] = None

class GetPipelineDefinitionInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    version: Optional[str] = None

class InstanceIdentityTypeDef(BaseValidatorModel):
    document: Optional[str] = None
    signature: Optional[str] = None

class ListPipelinesInputRequestTypeDef(BaseValidatorModel):
    marker: Optional[str] = None

class PipelineIdNameTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class OperatorTypeDef(BaseValidatorModel):
    type: Optional[OperatorTypeType] = None
    values: Optional[Sequence[str]] = None

class ParameterAttributeTypeDef(BaseValidatorModel):
    key: str
    stringValue: str

class ValidationErrorTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    errors: Optional[List[str]] = None

class ValidationWarningTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    warnings: Optional[List[str]] = None

class RemoveTagsInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    tagKeys: Sequence[str]

class ReportTaskRunnerHeartbeatInputRequestTypeDef(BaseValidatorModel):
    taskrunnerId: str
    workerGroup: Optional[str] = None
    hostname: Optional[str] = None

class SetStatusInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    status: str

class SetTaskStatusInputRequestTypeDef(BaseValidatorModel):
    taskId: str
    taskStatus: TaskStatusType
    errorId: Optional[str] = None
    errorMessage: Optional[str] = None
    errorStackTrace: Optional[str] = None

class ActivatePipelineInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None
    startTimestamp: Optional[TimestampTypeDef] = None

class AddTagsInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    tags: Sequence[TagTypeDef]

class CreatePipelineInputRequestTypeDef(BaseValidatorModel):
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

class DescribeObjectsInputDescribeObjectsPaginateTypeDef(BaseValidatorModel):
    pipelineId: str
    objectIds: Sequence[str]
    evaluateExpressions: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesInputListPipelinesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PipelineDescriptionTypeDef(BaseValidatorModel):
    pipelineId: str
    name: str
    fields: List[FieldTypeDef]
    description: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class PipelineObjectTypeDef(BaseValidatorModel):
    id: str
    name: str
    fields: List[FieldTypeDef]

class ReportTaskProgressInputRequestTypeDef(BaseValidatorModel):
    taskId: str
    fields: Optional[Sequence[FieldTypeDef]] = None

class PollForTaskInputRequestTypeDef(BaseValidatorModel):
    workerGroup: str
    hostname: Optional[str] = None
    instanceIdentity: Optional[InstanceIdentityTypeDef] = None

class ListPipelinesOutputTypeDef(BaseValidatorModel):
    pipelineIdList: List[PipelineIdNameTypeDef]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SelectorTypeDef(BaseValidatorModel):
    fieldName: Optional[str] = None
    operator: Optional[OperatorTypeDef] = None

class ParameterObjectTypeDef(BaseValidatorModel):
    id: str
    attributes: List[ParameterAttributeTypeDef]

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

class DescribeObjectsOutputTypeDef(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectTypeDef]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: ResponseMetadataTypeDef

class TaskObjectTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    pipelineId: Optional[str] = None
    attemptId: Optional[str] = None
    objects: Optional[Dict[str, PipelineObjectTypeDef]] = None

class QueryTypeDef(BaseValidatorModel):
    selectors: Optional[Sequence[SelectorTypeDef]] = None

class GetPipelineDefinitionOutputTypeDef(BaseValidatorModel):
    pipelineObjects: List[PipelineObjectTypeDef]
    parameterObjects: List[ParameterObjectTypeDef]
    parameterValues: List[ParameterValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPipelineDefinitionInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectTypeDef]
    parameterObjects: Optional[Sequence[ParameterObjectTypeDef]] = None
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None

class ValidatePipelineDefinitionInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    pipelineObjects: Sequence[PipelineObjectTypeDef]
    parameterObjects: Optional[Sequence[ParameterObjectTypeDef]] = None
    parameterValues: Optional[Sequence[ParameterValueTypeDef]] = None

class PollForTaskOutputTypeDef(BaseValidatorModel):
    taskObject: TaskObjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryObjectsInputQueryObjectsPaginateTypeDef(BaseValidatorModel):
    pipelineId: str
    sphere: str
    query: Optional[QueryTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryObjectsInputRequestTypeDef(BaseValidatorModel):
    pipelineId: str
    sphere: str
    query: Optional[QueryTypeDef] = None
    marker: Optional[str] = None
    limit: Optional[int] = None

