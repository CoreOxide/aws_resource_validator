from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pricing.pricing_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AttributeValue(BaseValidatorModel):
    Value: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_services' function.
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


class Filter(BaseValidatorModel):
    Type: Literal['TERM_MATCH']
    Field: str
    Value: str


# This class is the input for the 'get_attribute_values' function.
class GetAttributeValuesRequest(BaseValidatorModel):
    ServiceCode: str
    AttributeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'get_price_list_file_url' function.
class GetPriceListFileUrlRequest(BaseValidatorModel):
    PriceListArn: str
    FileFormat: str

Timestamp = Union[datetime, str]


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


# This class is the output for the 'get_attribute_values' function.
class GetAttributeValuesResponse(BaseValidatorModel):
    AttributeValues: List[AttributeValue]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_price_list_file_url' function.
class GetPriceListFileUrlResponse(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_products' function.
class GetProductsResponse(BaseValidatorModel):
    FormatVersion: str
    PriceList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_services' function.
class DescribeServicesResponse(BaseValidatorModel):
    Services: List[Service]
    FormatVersion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetProductsRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[List[Filter]] = None
    FormatVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_products' function.
class GetProductsRequest(BaseValidatorModel):
    ServiceCode: str
    Filters: Optional[List[Filter]] = None
    FormatVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPriceListsRequestPaginate(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: Timestamp
    CurrencyCode: str
    RegionCode: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_price_lists' function.
class ListPriceListsRequest(BaseValidatorModel):
    ServiceCode: str
    EffectiveDate: Timestamp
    CurrencyCode: str
    RegionCode: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_price_lists' function.
class ListPriceListsResponse(BaseValidatorModel):
    PriceLists: List[PriceList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None