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
from aws_resource_validator.pydantic_models.cloudfront_keyvaluestore_constants import *

class DeleteKeyRequestListItemTypeDef(BaseModel):
    Key: str

class DeleteKeyRequestRequestTypeDef(BaseModel):
    KvsARN: str
    Key: str
    IfMatch: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeKeyValueStoreRequestRequestTypeDef(BaseModel):
    KvsARN: str

class GetKeyRequestRequestTypeDef(BaseModel):
    KvsARN: str
    Key: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListKeysRequestRequestTypeDef(BaseModel):
    KvsARN: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListKeysResponseListItemTypeDef(BaseModel):
    Key: str
    Value: str

class PutKeyRequestListItemTypeDef(BaseModel):
    Key: str
    Value: str

class PutKeyRequestRequestTypeDef(BaseModel):
    Key: str
    Value: str
    KvsARN: str
    IfMatch: str

class DeleteKeyResponseTypeDef(BaseModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyValueStoreResponseTypeDef(BaseModel):
    ItemCount: int
    TotalSizeInBytes: int
    KvsARN: str
    Created: datetime
    ETag: str
    LastModified: datetime
    Status: str
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyResponseTypeDef(BaseModel):
    Key: str
    Value: str
    ItemCount: int
    TotalSizeInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutKeyResponseTypeDef(BaseModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKeysResponseTypeDef(BaseModel):
    ItemCount: int
    TotalSizeInBytes: int
    ETag: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeysRequestListKeysPaginateTypeDef(BaseModel):
    KvsARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysResponseTypeDef(BaseModel):
    NextToken: str
    Items: List[ListKeysResponseListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKeysRequestRequestTypeDef(BaseModel):
    KvsARN: str
    IfMatch: str
    Puts: Optional[Sequence[PutKeyRequestListItemTypeDef]] = None
    Deletes: Optional[Sequence[DeleteKeyRequestListItemTypeDef]] = None

