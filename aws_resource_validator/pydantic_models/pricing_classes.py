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

class AttributeValue(BaseValidatorModel):
    Value: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeServicesRequest(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Service(BaseValidatorModel):
    ServiceCode: str
    AttributeNames: Optional[List[str]] = None


class GetAttributeValuesRequest(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetPriceListFileUrlRequest(BaseValidatorModel):
    PriceListArn: str
    FileFormat: str


class PriceList(BaseValidatorModel):
    PriceListArn: Optional[str] = None
    RegionCode: Optional[str] = None
    CurrencyCode: Optional[str] = None
    FileFormats: Optional[List[str]] = None


class DescribeServicesRequestPaginate(BaseValidatorModel):
    ServiceCode: Optional[str] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAttributeValuesRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAttributeValuesResponse(BaseValidatorModel):
    AttributeValues: List[AttributeValue]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetPriceListFileUrlResponse(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


class GetProductsResponse(BaseValidatorModel):
    FormatVersion: str
    PriceList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeServicesResponse(BaseValidatorModel):
    Services: List[Service]
    FormatVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Filter(BaseValidatorModel):
    pass


class GetProductsRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[Sequence[Filter]] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetProductsRequest(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[Sequence[Filter]] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Timestamp(BaseValidatorModel):
    pass


class ListPriceListsRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: Timestamp
    CurrencyCode: str
    RegionCode: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPriceListsRequest(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: Timestamp
    CurrencyCode: str
    RegionCode: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPriceListsResponse(BaseValidatorModel):
    PriceLists: List[PriceList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


