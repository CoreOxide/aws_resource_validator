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
from aws_resource_validator.pydantic_models.cloudcontrol_constants import *

class CancelResourceRequestInputRequestTypeDef(BaseModel):
    RequestToken: str

class ProgressEventTypeDef(BaseModel):
    TypeName: Optional[str] = None
    Identifier: Optional[str] = None
    RequestToken: Optional[str] = None
    Operation: Optional[OperationType] = None
    OperationStatus: Optional[OperationStatusType] = None
    EventTime: Optional[datetime] = None
    ResourceModel: Optional[str] = None
    StatusMessage: Optional[str] = None
    ErrorCode: Optional[HandlerErrorCodeType] = None
    RetryAfter: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateResourceInputRequestTypeDef(BaseModel):
    TypeName: str
    DesiredState: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None

class DeleteResourceInputRequestTypeDef(BaseModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None

class GetResourceInputRequestTypeDef(BaseModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None

class ResourceDescriptionTypeDef(BaseModel):
    Identifier: Optional[str] = None
    Properties: Optional[str] = None

class GetResourceRequestStatusInputRequestTypeDef(BaseModel):
    RequestToken: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ResourceRequestStatusFilterTypeDef(BaseModel):
    Operations: Optional[Sequence[OperationType]] = None
    OperationStatuses: Optional[Sequence[OperationStatusType]] = None

class ListResourcesInputRequestTypeDef(BaseModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceModel: Optional[str] = None

class UpdateResourceInputRequestTypeDef(BaseModel):
    TypeName: str
    Identifier: str
    PatchDocument: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None

class CancelResourceRequestOutputTypeDef(BaseModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceOutputTypeDef(BaseModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourceOutputTypeDef(BaseModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceRequestStatusOutputTypeDef(BaseModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceRequestsOutputTypeDef(BaseModel):
    ResourceRequestStatusSummaries: List[ProgressEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceOutputTypeDef(BaseModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceOutputTypeDef(BaseModel):
    TypeName: str
    ResourceDescription: ResourceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesOutputTypeDef(BaseModel):
    TypeName: str
    ResourceDescriptions: List[ResourceDescriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceRequestStatusInputResourceRequestSuccessWaitTypeDef(BaseModel):
    RequestToken: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListResourcesInputListResourcesPaginateTypeDef(BaseModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ResourceModel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceRequestsInputListResourceRequestsPaginateTypeDef(BaseModel):
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceRequestsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilterTypeDef] = None

