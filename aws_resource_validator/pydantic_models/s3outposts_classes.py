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
from aws_resource_validator.pydantic_models.s3outposts_constants import *

class CreateEndpointRequestTypeDef(BaseValidatorModel):
    OutpostId: str
    SubnetId: str
    SecurityGroupId: str
    AccessType: Optional[EndpointAccessTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteEndpointRequestTypeDef(BaseValidatorModel):
    EndpointId: str
    OutpostId: str


class FailedReasonTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEndpointsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOutpostsWithS3RequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OutpostTypeDef(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    S3OutpostArn: Optional[str] = None
    OutpostId: Optional[str] = None
    OwnerId: Optional[str] = None
    CapacityInBytes: Optional[int] = None


class ListSharedEndpointsRequestTypeDef(BaseValidatorModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CreateEndpointResultTypeDef(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointTypeDef(BaseValidatorModel):
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


class ListEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOutpostsWithS3RequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSharedEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOutpostsWithS3ResultTypeDef(BaseValidatorModel):
    Outposts: List[OutpostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEndpointsResultTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSharedEndpointsResultTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


