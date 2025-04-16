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
from aws_resource_validator.pydantic_models.marketplace_entitlement_constants import *

class EntitlementValue(BaseValidatorModel):
    IntegerValue: Optional[int] = None
    DoubleValue: Optional[float] = None
    BooleanValue: Optional[bool] = None
    StringValue: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetEntitlementsRequest(BaseValidatorModel):
    ProductCode: str
    Filter: Optional[Mapping[GetEntitlementFilterNameType, Sequence[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Entitlement(BaseValidatorModel):
    ProductCode: Optional[str] = None
    Dimension: Optional[str] = None
    CustomerIdentifier: Optional[str] = None
    Value: Optional[EntitlementValue] = None
    ExpirationDate: Optional[datetime] = None


class GetEntitlementsRequestPaginate(BaseValidatorModel):
    ProductCode: str
    Filter: Optional[Mapping[GetEntitlementFilterNameType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetEntitlementsResult(BaseValidatorModel):
    Entitlements: List[Entitlement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


