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
from aws_resource_validator.pydantic_models.sdb_constants import *

class AttributeTypeDef(BaseModel):
    Name: str
    Value: str
    AlternateNameEncoding: Optional[str] = None
    AlternateValueEncoding: Optional[str] = None

class CreateDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class UpdateConditionTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Exists: Optional[bool] = None

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DomainMetadataRequestRequestTypeDef(BaseModel):
    DomainName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetAttributesRequestRequestTypeDef(BaseModel):
    DomainName: str
    ItemName: str
    AttributeNames: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    MaxNumberOfDomains: Optional[int] = None
    NextToken: Optional[str] = None

class ReplaceableAttributeTypeDef(BaseModel):
    Name: str
    Value: str
    Replace: Optional[bool] = None

class SelectRequestRequestTypeDef(BaseModel):
    SelectExpression: str
    NextToken: Optional[str] = None
    ConsistentRead: Optional[bool] = None

class DeletableItemTypeDef(BaseModel):
    Name: str
    Attributes: Optional[Sequence[AttributeTypeDef]] = None

class ItemTypeDef(BaseModel):
    Name: str
    Attributes: List[AttributeTypeDef]
    AlternateNameEncoding: Optional[str] = None

class DeleteAttributesRequestRequestTypeDef(BaseModel):
    DomainName: str
    ItemName: str
    Attributes: Optional[Sequence[AttributeTypeDef]] = None
    Expected: Optional[UpdateConditionTypeDef] = None

class DomainMetadataResultTypeDef(BaseModel):
    ItemCount: int
    ItemNamesSizeBytes: int
    AttributeNameCount: int
    AttributeNamesSizeBytes: int
    AttributeValueCount: int
    AttributeValuesSizeBytes: int
    Timestamp: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttributesResultTypeDef(BaseModel):
    Attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResultTypeDef(BaseModel):
    DomainNames: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsRequestListDomainsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SelectRequestSelectPaginateTypeDef(BaseModel):
    SelectExpression: str
    ConsistentRead: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PutAttributesRequestRequestTypeDef(BaseModel):
    DomainName: str
    ItemName: str
    Attributes: Sequence[ReplaceableAttributeTypeDef]
    Expected: Optional[UpdateConditionTypeDef] = None

class ReplaceableItemTypeDef(BaseModel):
    Name: str
    Attributes: Sequence[ReplaceableAttributeTypeDef]

class BatchDeleteAttributesRequestRequestTypeDef(BaseModel):
    DomainName: str
    Items: Sequence[DeletableItemTypeDef]

class SelectResultTypeDef(BaseModel):
    Items: List[ItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutAttributesRequestRequestTypeDef(BaseModel):
    DomainName: str
    Items: Sequence[ReplaceableItemTypeDef]

