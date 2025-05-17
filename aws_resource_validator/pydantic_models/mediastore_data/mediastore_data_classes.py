from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediastore_data.mediastore_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class DeleteObjectRequest(BaseValidatorModel):
    Path: str


# This class is the input for the 'describe_object' function.
class DescribeObjectRequest(BaseValidatorModel):
    Path: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_object' function.
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


# This class is the input for the 'list_items' function.
class ListItemsRequest(BaseValidatorModel):
    Path: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'put_object' function.
class PutObjectRequest(BaseValidatorModel):
    Body: Blob
    Path: str
    ContentType: Optional[str] = None
    CacheControl: Optional[str] = None
    StorageClass: Optional[Literal['TEMPORAL']] = None
    UploadAvailability: Optional[UploadAvailabilityType] = None


# This class is the output for the 'describe_object' function.
class DescribeObjectResponse(BaseValidatorModel):
    ETag: str
    ContentType: str
    ContentLength: int
    CacheControl: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_object' function.
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


# This class is the output for the 'put_object' function.
class PutObjectResponse(BaseValidatorModel):
    ContentSHA256: str
    ETag: str
    StorageClass: Literal['TEMPORAL']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_items' function.
class ListItemsResponse(BaseValidatorModel):
    Items: List[Item]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListItemsRequestPaginate(BaseValidatorModel):
    Path: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None