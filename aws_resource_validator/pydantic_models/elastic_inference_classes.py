from datetime import datetime
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
from aws_resource_validator.pydantic_models.elastic_inference_constants import *

class AcceleratorTypeOfferingTypeDef(BaseValidatorModel):
    acceleratorType: Optional[str] = None
    locationType: Optional[LocationTypeType] = None
    location: Optional[str] = None

class KeyValuePairTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[int] = None

class MemoryInfoTypeDef(BaseValidatorModel):
    sizeInMiB: Optional[int] = None

class DescribeAcceleratorOfferingsRequestRequestTypeDef(BaseValidatorModel):
    locationType: LocationTypeType
    acceleratorTypes: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ElasticInferenceAcceleratorHealthTypeDef(BaseValidatorModel):
    status: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AcceleratorTypeTypeDef(BaseValidatorModel):
    acceleratorTypeName: Optional[str] = None
    memoryInfo: Optional[MemoryInfoTypeDef] = None
    throughputInfo: Optional[List[KeyValuePairTypeDef]] = None

class DescribeAcceleratorOfferingsResponseTypeDef(BaseValidatorModel):
    acceleratorTypeOfferings: List[AcceleratorTypeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorsRequestRequestTypeDef(BaseValidatorModel):
    acceleratorIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeAcceleratorsRequestDescribeAcceleratorsPaginateTypeDef(BaseValidatorModel):
    acceleratorIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ElasticInferenceAcceleratorTypeDef(BaseValidatorModel):
    acceleratorHealth: Optional[ElasticInferenceAcceleratorHealthTypeDef] = None
    acceleratorType: Optional[str] = None
    acceleratorId: Optional[str] = None
    availabilityZone: Optional[str] = None
    attachedResource: Optional[str] = None

class DescribeAcceleratorTypesResponseTypeDef(BaseValidatorModel):
    acceleratorTypes: List[AcceleratorTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorsResponseTypeDef(BaseValidatorModel):
    acceleratorSet: List[ElasticInferenceAcceleratorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

