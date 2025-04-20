from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    Puts: Optional[List[PutKeyRequestListItem]] = None
    Deletes: Optional[List[DeleteKeyRequestListItem]] = None