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
from aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_constants import *

class DeleteKeyRequestListItem(BaseValidatorModel):
    Key: str


class DeleteKeyRequest(BaseValidatorModel):
    KvsARN: str
    Key: str
    IfMatch: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeKeyValueStoreRequest(BaseValidatorModel):
    KvsARN: str


class GetKeyRequest(BaseValidatorModel):
    KvsARN: str
    Key: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListKeysRequest(BaseValidatorModel):
    KvsARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListKeysResponseListItem(BaseValidatorModel):
    Key: str
    Value: str


class PutKeyRequestListItem(BaseValidatorModel):
    Key: str
    Value: str


class PutKeyRequest(BaseValidatorModel):
    Key: str
    Value: str
    KvsARN: str
    IfMatch: str


class DeleteKeyResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadata


class DescribeKeyValueStoreResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    KvsARN: str
    Created: datetime
    ETag: str
    LastModified: datetime
    Status: str
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class GetKeyResponse(BaseValidatorModel):
    Key: str
    Value: str
    ItemCount: int
    TotalSizeInBytes: int
    ResponseMetadata: ResponseMetadata


class PutKeyResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadata


class UpdateKeysResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadata


class ListKeysRequestPaginate(BaseValidatorModel):
    KvsARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeysResponse(BaseValidatorModel):
    Items: List[ListKeysResponseListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateKeysRequest(BaseValidatorModel):
    KvsARN: str
    IfMatch: str
    Puts: Optional[Sequence[PutKeyRequestListItem]] = None
    Deletes: Optional[Sequence[DeleteKeyRequestListItem]] = None


