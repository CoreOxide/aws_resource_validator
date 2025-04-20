from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudcontrol.cloudcontrol_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CancelResourceRequestInput(BaseValidatorModel):
    RequestToken: str


class ProgressEvent(BaseValidatorModel):
    TypeName: Optional[str] = None
    Identifier: Optional[str] = None
    RequestToken: Optional[str] = None
    HooksRequestToken: Optional[str] = None
    Operation: Optional[OperationType] = None
    OperationStatus: Optional[OperationStatusType] = None
    EventTime: Optional[datetime] = None
    ResourceModel: Optional[str] = None
    StatusMessage: Optional[str] = None
    ErrorCode: Optional[HandlerErrorCodeType] = None
    RetryAfter: Optional[datetime] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateResourceInput(BaseValidatorModel):
    TypeName: str
    DesiredState: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None


class DeleteResourceInput(BaseValidatorModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None


class GetResourceInput(BaseValidatorModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None


class ResourceDescription(BaseValidatorModel):
    Identifier: Optional[str] = None
    Properties: Optional[str] = None


class GetResourceRequestStatusInput(BaseValidatorModel):
    RequestToken: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class HookProgressEvent(BaseValidatorModel):
    HookTypeName: Optional[str] = None
    HookTypeVersionId: Optional[str] = None
    HookTypeArn: Optional[str] = None
    InvocationPoint: Optional[str] = None
    HookStatus: Optional[str] = None
    HookEventTime: Optional[datetime] = None
    HookStatusMessage: Optional[str] = None
    FailureMode: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResourceRequestStatusFilter(BaseValidatorModel):
    Operations: Optional[List[OperationType]] = None
    OperationStatuses: Optional[List[OperationStatusType]] = None


class ListResourcesInput(BaseValidatorModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceModel: Optional[str] = None


class UpdateResourceInput(BaseValidatorModel):
    TypeName: str
    Identifier: str
    PatchDocument: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None


class CancelResourceRequestOutput(BaseValidatorModel):
    ProgressEvent: ProgressEvent
    ResponseMetadata: ResponseMetadata


class CreateResourceOutput(BaseValidatorModel):
    ProgressEvent: ProgressEvent
    ResponseMetadata: ResponseMetadata


class DeleteResourceOutput(BaseValidatorModel):
    ProgressEvent: ProgressEvent
    ResponseMetadata: ResponseMetadata


class ListResourceRequestsOutput(BaseValidatorModel):
    ResourceRequestStatusSummaries: List[ProgressEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateResourceOutput(BaseValidatorModel):
    ProgressEvent: ProgressEvent
    ResponseMetadata: ResponseMetadata


class GetResourceOutput(BaseValidatorModel):
    TypeName: str
    ResourceDescription: ResourceDescription
    ResponseMetadata: ResponseMetadata


class ListResourcesOutput(BaseValidatorModel):
    TypeName: str
    ResourceDescriptions: List[ResourceDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetResourceRequestStatusInputWait(BaseValidatorModel):
    RequestToken: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetResourceRequestStatusOutput(BaseValidatorModel):
    ProgressEvent: ProgressEvent
    HooksProgressEvent: List[HookProgressEvent]
    ResponseMetadata: ResponseMetadata


class ListResourcesInputPaginate(BaseValidatorModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ResourceModel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceRequestsInputPaginate(BaseValidatorModel):
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceRequestsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilter] = None