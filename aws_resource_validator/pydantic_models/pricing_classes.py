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
from aws_resource_validator.pydantic_models.pricing_constants import *

class AttributeValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeServicesRequestTypeDef(BaseValidatorModel):
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


class GetAttributeValuesRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetPriceListFileUrlRequestTypeDef(BaseValidatorModel):
    PriceListArn: str
    FileFormat: str


class PriceListTypeDef(BaseValidatorModel):
    PriceListArn: Optional[str] = None
    RegionCode: Optional[str] = None
    CurrencyCode: Optional[str] = None
    FileFormats: Optional[List[str]] = None


class DescribeServicesRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAttributeValuesRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAttributeValuesResponseTypeDef(BaseValidatorModel):
    AttributeValues: List[AttributeValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetPriceListFileUrlResponseTypeDef(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetProductsResponseTypeDef(BaseValidatorModel):
    FormatVersion: str
    PriceList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeServicesResponseTypeDef(BaseValidatorModel):
    Services: List[ServiceTypeDef]
    FormatVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    pass


class GetProductsRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetProductsRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListPriceListsRequestPaginateTypeDef(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: TimestampTypeDef
    CurrencyCode: str
    RegionCode: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPriceListsRequestTypeDef(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: TimestampTypeDef
    CurrencyCode: str
    RegionCode: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPriceListsResponseTypeDef(BaseValidatorModel):
    PriceLists: List[PriceListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


