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
from aws_resource_validator.pydantic_models.pricing_constants import *

class AttributeValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeServicesRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ServiceTypeDef(BaseValidatorModel):
    ServiceCode: str
    AttributeNames: Optional[List[str]] = None

class FilterTypeDef(BaseValidatorModel):
    Type: Literal["TERM_MATCH"]
    Field: str
    Value: str

class GetAttributeValuesRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetPriceListFileUrlRequestRequestTypeDef(BaseValidatorModel):
    PriceListArn: str
    FileFormat: str

class PriceListTypeDef(BaseValidatorModel):
    PriceListArn: Optional[str] = None
    RegionCode: Optional[str] = None
    CurrencyCode: Optional[str] = None
    FileFormats: Optional[List[str]] = None

class DescribeServicesRequestDescribeServicesPaginateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAttributeValuesRequestGetAttributeValuesPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAttributeValuesResponseTypeDef(BaseValidatorModel):
    AttributeValues: List[AttributeValueTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPriceListFileUrlResponseTypeDef(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProductsResponseTypeDef(BaseValidatorModel):
    FormatVersion: str
    PriceList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServicesResponseTypeDef(BaseValidatorModel):
    Services: List[ServiceTypeDef]
    FormatVersion: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProductsRequestGetProductsPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetProductsRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPriceListsRequestListPriceListsPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: TimestampTypeDef
    CurrencyCode: str
    RegionCode: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPriceListsRequestRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: TimestampTypeDef
    CurrencyCode: str
    RegionCode: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPriceListsResponseTypeDef(BaseValidatorModel):
    PriceLists: List[PriceListTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

