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
from aws_resource_validator.pydantic_models.mediastore_data_constants import *

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


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListItemsRequest(BaseValidatorModel):
    Path: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class PutObjectRequest(BaseValidatorModel):
    Body: Blob
    Path: str
    ContentType: Optional[str] = None
    CacheControl: Optional[str] = None
    StorageClass: Optional[Literal["TEMPORAL"]] = None
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
    StorageClass: Literal["TEMPORAL"]
    ResponseMetadata: ResponseMetadata


class Item(BaseValidatorModel):
    pass


class ListItemsResponse(BaseValidatorModel):
    Items: List[Item]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListItemsRequestPaginate(BaseValidatorModel):
    Path: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


