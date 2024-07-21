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
from aws_resource_validator.pydantic_models.elastic_inference_constants import *

class AcceleratorTypeOfferingTypeDef(BaseModel):
    acceleratorType: Optional[str] = None
    locationType: Optional[LocationTypeType] = None
    location: Optional[str] = None

class KeyValuePairTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[int] = None

class MemoryInfoTypeDef(BaseModel):
    sizeInMiB: Optional[int] = None

class DescribeAcceleratorOfferingsRequestRequestTypeDef(BaseModel):
    locationType: LocationTypeType
    acceleratorTypes: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FilterTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ElasticInferenceAcceleratorHealthTypeDef(BaseModel):
    status: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AcceleratorTypeTypeDef(BaseModel):
    acceleratorTypeName: Optional[str] = None
    memoryInfo: Optional[MemoryInfoTypeDef] = None
    throughputInfo: Optional[List[KeyValuePairTypeDef]] = None

class DescribeAcceleratorOfferingsResponseTypeDef(BaseModel):
    acceleratorTypeOfferings: List[AcceleratorTypeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorsRequestRequestTypeDef(BaseModel):
    acceleratorIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeAcceleratorsRequestDescribeAcceleratorsPaginateTypeDef(BaseModel):
    acceleratorIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ElasticInferenceAcceleratorTypeDef(BaseModel):
    acceleratorHealth: Optional[ElasticInferenceAcceleratorHealthTypeDef] = None
    acceleratorType: Optional[str] = None
    acceleratorId: Optional[str] = None
    availabilityZone: Optional[str] = None
    attachedResource: Optional[str] = None

class DescribeAcceleratorTypesResponseTypeDef(BaseModel):
    acceleratorTypes: List[AcceleratorTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorsResponseTypeDef(BaseModel):
    acceleratorSet: List[ElasticInferenceAcceleratorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

