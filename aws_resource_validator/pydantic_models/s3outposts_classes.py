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
from aws_resource_validator.pydantic_models.s3outposts_constants import *

class CreateEndpointRequestRequestTypeDef(BaseModel):
    OutpostId: str
    SubnetId: str
    SecurityGroupId: str
    AccessType: Optional[EndpointAccessTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteEndpointRequestRequestTypeDef(BaseModel):
    EndpointId: str
    OutpostId: str

class FailedReasonTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class NetworkInterfaceTypeDef(BaseModel):
    NetworkInterfaceId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEndpointsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListOutpostsWithS3RequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OutpostTypeDef(BaseModel):
    OutpostArn: Optional[str] = None
    S3OutpostArn: Optional[str] = None
    OutpostId: Optional[str] = None
    OwnerId: Optional[str] = None
    CapacityInBytes: Optional[int] = None

class ListSharedEndpointsRequestRequestTypeDef(BaseModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class CreateEndpointResultTypeDef(BaseModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointTypeDef(BaseModel):
    EndpointArn: Optional[str] = None
    OutpostsId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Status: Optional[EndpointStatusType] = None
    CreationTime: Optional[datetime] = None
    NetworkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    AccessType: Optional[EndpointAccessTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    FailedReason: Optional[FailedReasonTypeDef] = None

class ListEndpointsRequestListEndpointsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutpostsWithS3RequestListOutpostsWithS3PaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSharedEndpointsRequestListSharedEndpointsPaginateTypeDef(BaseModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutpostsWithS3ResultTypeDef(BaseModel):
    Outposts: List[OutpostTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointsResultTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSharedEndpointsResultTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

