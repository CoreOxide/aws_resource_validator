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
from aws_resource_validator.pydantic_models.marketplace_entitlement_constants import *

class EntitlementValueTypeDef(BaseModel):
    IntegerValue: Optional[int] = None
    DoubleValue: Optional[float] = None
    BooleanValue: Optional[bool] = None
    StringValue: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetEntitlementsRequestRequestTypeDef(BaseModel):
    ProductCode: str
    Filter: Optional[Mapping[GetEntitlementFilterNameType, Sequence[str]]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class EntitlementTypeDef(BaseModel):
    ProductCode: Optional[str] = None
    Dimension: Optional[str] = None
    CustomerIdentifier: Optional[str] = None
    Value: Optional[EntitlementValueTypeDef] = None
    ExpirationDate: Optional[datetime] = None

class GetEntitlementsRequestGetEntitlementsPaginateTypeDef(BaseModel):
    ProductCode: str
    Filter: Optional[Mapping[GetEntitlementFilterNameType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEntitlementsResultTypeDef(BaseModel):
    Entitlements: List[EntitlementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

