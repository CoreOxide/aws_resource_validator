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

class DeleteKeyRequestListItemTypeDef(BaseValidatorModel):
    Key: str


class DeleteKeyRequestTypeDef(BaseValidatorModel):
    KvsARN: str
    Key: str
    IfMatch: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeKeyValueStoreRequestTypeDef(BaseValidatorModel):
    KvsARN: str


class GetKeyRequestTypeDef(BaseValidatorModel):
    KvsARN: str
    Key: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListKeysRequestTypeDef(BaseValidatorModel):
    KvsARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListKeysResponseListItemTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class PutKeyRequestListItemTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class PutKeyRequestTypeDef(BaseValidatorModel):
    Key: str
    Value: str
    KvsARN: str
    IfMatch: str


class DeleteKeyResponseTypeDef(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeKeyValueStoreResponseTypeDef(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    KvsARN: str
    Created: datetime
    ETag: str
    LastModified: datetime
    Status: str
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetKeyResponseTypeDef(BaseValidatorModel):
    Key: str
    Value: str
    ItemCount: int
    TotalSizeInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef


class PutKeyResponseTypeDef(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateKeysResponseTypeDef(BaseValidatorModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListKeysRequestPaginateTypeDef(BaseValidatorModel):
    KvsARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKeysResponseTypeDef(BaseValidatorModel):
    Items: List[ListKeysResponseListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateKeysRequestTypeDef(BaseValidatorModel):
    KvsARN: str
    IfMatch: str
    Puts: Optional[Sequence[PutKeyRequestListItemTypeDef]] = None
    Deletes: Optional[Sequence[DeleteKeyRequestListItemTypeDef]] = None


