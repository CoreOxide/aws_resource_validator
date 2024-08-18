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
from aws_resource_validator.pydantic_models.cloudcontrol_constants import *

class CancelResourceRequestInputRequestTypeDef(BaseValidatorModel):
    RequestToken: str

class ProgressEventTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateResourceInputRequestTypeDef(BaseValidatorModel):
    TypeName: str
    DesiredState: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None

class DeleteResourceInputRequestTypeDef(BaseValidatorModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ClientToken: Optional[str] = None

class GetResourceInputRequestTypeDef(BaseValidatorModel):
    TypeName: str
    Identifier: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None

class ResourceDescriptionTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    Properties: Optional[str] = None

class GetResourceRequestStatusInputRequestTypeDef(BaseValidatorModel):
    RequestToken: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ResourceRequestStatusFilterTypeDef(BaseValidatorModel):
    Operations: Optional[Sequence[OperationType]] = None
    OperationStatuses: Optional[Sequence[OperationStatusType]] = None

class ListResourcesInputRequestTypeDef(BaseValidatorModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceModel: Optional[str] = None

class UpdateResourceInputRequestTypeDef(BaseValidatorModel):
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

class GetResourceRequestStatusOutputTypeDef(BaseValidatorModel):
    ProgressEvent: ProgressEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceRequestsOutputTypeDef(BaseValidatorModel):
    ResourceRequestStatusSummaries: List[ProgressEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceRequestStatusInputResourceRequestSuccessWaitTypeDef(BaseValidatorModel):
    RequestToken: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListResourcesInputListResourcesPaginateTypeDef(BaseValidatorModel):
    TypeName: str
    TypeVersionId: Optional[str] = None
    RoleArn: Optional[str] = None
    ResourceModel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceRequestsInputListResourceRequestsPaginateTypeDef(BaseValidatorModel):
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceRequestsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceRequestStatusFilter: Optional[ResourceRequestStatusFilterTypeDef] = None

