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
from aws_resource_validator.pydantic_models.pricing_constants import *

class AttributeValueTypeDef(BaseModel):
    Value: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeServicesRequestRequestTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ServiceTypeDef(BaseModel):
    ServiceCode: str
    AttributeNames: Optional[List[str]] = None

class FilterTypeDef(BaseModel):
    Type: Literal["TERM_MATCH"]
    Field: str
    Value: str

class GetAttributeValuesRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    AttributeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetPriceListFileUrlRequestRequestTypeDef(BaseModel):
    PriceListArn: str
    FileFormat: str

class PriceListTypeDef(BaseModel):
    PriceListArn: Optional[str] = None
    RegionCode: Optional[str] = None
    CurrencyCode: Optional[str] = None
    FileFormats: Optional[List[str]] = None

class DescribeServicesRequestDescribeServicesPaginateTypeDef(BaseModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAttributeValuesRequestGetAttributeValuesPaginateTypeDef(BaseModel):
    ServiceCode: str
    AttributeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAttributeValuesResponseTypeDef(BaseModel):
    AttributeValues: List[AttributeValueTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPriceListFileUrlResponseTypeDef(BaseModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProductsResponseTypeDef(BaseModel):
    FormatVersion: str
    PriceList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServicesResponseTypeDef(BaseModel):
    Services: List[ServiceTypeDef]
    FormatVersion: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProductsRequestGetProductsPaginateTypeDef(BaseModel):
    ServiceCode: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetProductsRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPriceListsRequestListPriceListsPaginateTypeDef(BaseModel):
    ServiceCode: str
    EffectiveDate: TimestampTypeDef
    CurrencyCode: str
    RegionCode: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPriceListsRequestRequestTypeDef(BaseModel):
    ServiceCode: str
    EffectiveDate: TimestampTypeDef
    CurrencyCode: str
    RegionCode: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPriceListsResponseTypeDef(BaseModel):
    PriceLists: List[PriceListTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

