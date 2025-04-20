from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.s3outposts.s3outposts_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CreateEndpointRequest(BaseValidatorModel):
    OutpostId: str
    SubnetId: str
    SecurityGroupId: str
    AccessType: Optional[EndpointAccessTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteEndpointRequest(BaseValidatorModel):
    EndpointId: str
    OutpostId: str


class FailedReason(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEndpointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOutpostsWithS3Request(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Outpost(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    S3OutpostArn: Optional[str] = None
    OutpostId: Optional[str] = None
    OwnerId: Optional[str] = None
    CapacityInBytes: Optional[int] = None


class ListSharedEndpointsRequest(BaseValidatorModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CreateEndpointResult(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class Endpoint(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    OutpostsId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Status: Optional[EndpointStatusType] = None
    CreationTime: Optional[datetime] = None
    NetworkInterfaces: Optional[List[NetworkInterface]] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    AccessType: Optional[EndpointAccessTypeType] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    FailedReason: Optional[FailedReason] = None


class ListEndpointsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOutpostsWithS3RequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSharedEndpointsRequestPaginate(BaseValidatorModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOutpostsWithS3Result(BaseValidatorModel):
    Outposts: List[Outpost]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEndpointsResult(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSharedEndpointsResult(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None