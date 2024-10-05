from datetime import datetime

from botocore.response import StreamingBody

from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class DeleteObjectRequestRequestTypeDef(BaseValidatorModel):
    Path: str

class DescribeObjectRequestRequestTypeDef(BaseValidatorModel):
    Path: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetObjectRequestRequestTypeDef(BaseValidatorModel):
    Path: str
    Range: Optional[str] = None

class ItemTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[ItemTypeType] = None
    ETag: Optional[str] = None
    LastModified: Optional[datetime] = None
    ContentType: Optional[str] = None
    ContentLength: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListItemsRequestRequestTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PutObjectRequestRequestTypeDef(BaseValidatorModel):
    Body: BlobTypeDef
    Path: str
    ContentType: Optional[str] = None
    CacheControl: Optional[str] = None
    StorageClass: Optional[Literal["TEMPORAL"]] = None
    UploadAvailability: Optional[UploadAvailabilityType] = None

class DescribeObjectResponseTypeDef(BaseValidatorModel):
    ETag: str
    ContentType: str
    ContentLength: int
    CacheControl: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectResponseTypeDef(BaseValidatorModel):
    Body: StreamingBody
    CacheControl: str
    ContentRange: str
    ContentLength: int
    ContentType: str
    ETag: str
    LastModified: datetime
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectResponseTypeDef(BaseValidatorModel):
    ContentSHA256: str
    ETag: str
    StorageClass: Literal["TEMPORAL"]
    ResponseMetadata: ResponseMetadataTypeDef

class ListItemsResponseTypeDef(BaseValidatorModel):
    Items: List[ItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListItemsRequestListItemsPaginateTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

