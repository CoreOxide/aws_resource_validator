from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudfront_keyvaluestore.cloudfront_keyvaluestore_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeleteKeyRequestListItem(BaseValidatorModel):
    Key: str


# This class is the input for the 'delete_key' function.
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


# This class is the input for the 'describe_key_value_store' function.
class DescribeKeyValueStoreRequest(BaseValidatorModel):
    KvsARN: str


# This class is the input for the 'get_key' function.
class GetKeyRequest(BaseValidatorModel):
    KvsARN: str
    Key: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_keys' function.
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


# This class is the input for the 'put_key' function.
class PutKeyRequest(BaseValidatorModel):
    Key: str
    Value: str
    KvsARN: str
    IfMatch: str


# This class is the output for the 'delete_key' function.
class DeleteKeyResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_key_value_store' function.
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


# This class is the output for the 'get_key' function.
class GetKeyResponse(BaseValidatorModel):
    Key: str
    Value: str
    ItemCount: int
    TotalSizeInBytes: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_key' function.
class PutKeyResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_keys' function.
class UpdateKeysResponse(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadata


class ListKeysRequestPaginate(BaseValidatorModel):
    KvsARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_keys' function.
class ListKeysResponse(BaseValidatorModel):
    Items: List[ListKeysResponseListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'update_keys' function.
class UpdateKeysRequest(BaseValidatorModel):
    KvsARN: str
    IfMatch: str
    Puts: Optional[List[PutKeyRequestListItem]] = None
    Deletes: Optional[List[DeleteKeyRequestListItem]] = None