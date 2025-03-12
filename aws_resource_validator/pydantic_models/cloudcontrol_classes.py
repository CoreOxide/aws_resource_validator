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
from aws_resource_validator.pydantic_models.cloudcontrol_constants import *

class CancelResourceRequestInputTypeDef(BaseValidatorModel):
    RequestToken: str


class ProgressEventTypeDef(BaseValidatorModel):
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


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateResourceInputTypeDef(BaseValidatorModel):
    TypeName: str
    DesiredState: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None


class DeleteResourceInputTypeDef(BaseValidatorModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None


class GetResourceInputTypeDef(BaseValidatorModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None


class ResourceDescriptionTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    Properties: Optional[str] = None


class GetResourceRequestStatusInputTypeDef(BaseValidatorModel):
    RequestToken: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class HookProgressEventTypeDef(BaseValidatorModel):
    HookTypeName: Optional[str] = None
    HookTypeVersionId: Optional[str] = None
    HookTypeArn: Optional[str] = None
    InvocationPoint: Optional[str] = None
    HookStatus: Optional[str] = None
    HookEventTime: Optional[datetime] = None
    HookStatusMessage: Optional[str] = None
    FailureMode: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResourceRequestStatusFilterTypeDef(BaseValidatorModel):
    Operations: Optional[Sequence[OperationType]] = None
    OperationStatuses: Optional[Sequence[OperationStatusType]] = None


class ListResourcesInputTypeDef(BaseValidatorModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceModel: Optional[str] = None


class UpdateResourceInputTypeDef(BaseValidatorModel):
    TypeName: str
    Identifier: str
    PatchDocument: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None


class CancelResourceRequestOutputTypeDef(BaseValidatorModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceOutputTypeDef(BaseValidatorModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResourceOutputTypeDef(BaseValidatorModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourceRequestsOutputTypeDef(BaseValidatorModel):
    ResourceRequestStatusSummaries: List[ProgressEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateResourceOutputTypeDef(BaseValidatorModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceOutputTypeDef(BaseValidatorModel):
    TypeName: str
    ResourceDescription: ResourceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourcesOutputTypeDef(BaseValidatorModel):
    TypeName: str
    ResourceDescriptions: List[ResourceDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetResourceRequestStatusInputWaitTypeDef(BaseValidatorModel):
    RequestToken: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetResourceRequestStatusOutputTypeDef(BaseValidatorModel):
    ProgressEvent: ProgressEventTypeDef
    HooksProgressEvent: List[HookProgressEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourcesInputPaginateTypeDef(BaseValidatorModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ResourceModel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceRequestsInputPaginateTypeDef(BaseValidatorModel):
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceRequestsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilterTypeDef] = None


