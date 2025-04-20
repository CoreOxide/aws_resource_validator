from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediastore_data.mediastore_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class DeleteObjectRequest(BaseValidatorModel):
    Path: str


class DescribeObjectRequest(BaseValidatorModel):
    Path: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetObjectRequest(BaseValidatorModel):
    Path: str
    Range: Optional[str] = None


class Item(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[ItemTypeType] = None
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ContentType: Optional[str] = None
    ContentLength: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListItemsRequest(BaseValidatorModel):
    Path: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PutObjectRequest(BaseValidatorModel):
    Body: Blob
    Path: str
    ContentType: Optional[str] = None
    CacheControl: Optional[str] = None
    StorageClass: Optional[Literal['TEMPORAL']] = None
    UploadAvailability: Optional[UploadAvailabilityType] = None


class DescribeObjectResponse(BaseValidatorModel):
    ETag: str
    ContentType: str
    ContentLength: int
    CacheControl: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadata


class GetObjectResponse(BaseValidatorModel):
    Body: StreamingBody
    CacheControl: str
    ContentRange: str
    ContentLength: int
    ContentType: str
    ETag: str
    LastModified: datetime
    StatusCode: int
    ResponseMetadata: ResponseMetadata


class PutObjectResponse(BaseValidatorModel):
    ContentSHA256: str
    ETag: str
    StorageClass: Literal['TEMPORAL']
    ResponseMetadata: ResponseMetadata


class ListItemsResponse(BaseValidatorModel):
    Items: List[Item]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListItemsRequestPaginate(BaseValidatorModel):
    Path: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None