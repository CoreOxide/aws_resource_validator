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
from aws_resource_validator.pydantic_models.mediastore_data_constants import *

class DeleteObjectRequestRequestTypeDef(BaseModel):
    Path: str

class DescribeObjectRequestRequestTypeDef(BaseModel):
    Path: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetObjectRequestRequestTypeDef(BaseModel):
    Path: str
    Range: Optional[str] = None

class ItemTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[ItemTypeType] = None
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ContentType: Optional[str] = None
    ContentLength: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListItemsRequestRequestTypeDef(BaseModel):
    Path: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PutObjectRequestRequestTypeDef(BaseModel):
    Body: BlobTypeDef
    Path: str
    ContentType: Optional[str] = None
    CacheControl: Optional[str] = None
    StorageClass: Optional[Literal["TEMPORAL"]] = None
    UploadAvailability: Optional[UploadAvailabilityType] = None

class DescribeObjectResponseTypeDef(BaseModel):
    ETag: str
    ContentType: str
    ContentLength: int
    CacheControl: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectResponseTypeDef(BaseModel):
    Body: StreamingBody
    CacheControl: str
    ContentRange: str
    ContentLength: int
    ContentType: str
    ETag: str
    LastModified: datetime
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectResponseTypeDef(BaseModel):
    ContentSHA256: str
    ETag: str
    StorageClass: Literal["TEMPORAL"]
    ResponseMetadata: ResponseMetadataTypeDef

class ListItemsResponseTypeDef(BaseModel):
    Items: List[ItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListItemsRequestListItemsPaginateTypeDef(BaseModel):
    Path: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

