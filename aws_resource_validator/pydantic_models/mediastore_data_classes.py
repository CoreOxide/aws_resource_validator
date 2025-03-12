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

class DeleteObjectRequestTypeDef(BaseValidatorModel):
    Path: str


class DescribeObjectRequestTypeDef(BaseValidatorModel):
    Path: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetObjectRequestTypeDef(BaseValidatorModel):
    Path: str
    Range: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListItemsRequestTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class PutObjectRequestTypeDef(BaseValidatorModel):
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


class ItemTypeDef(BaseValidatorModel):
    pass


class ListItemsResponseTypeDef(BaseValidatorModel):
    Items: List[ItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListItemsRequestPaginateTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


