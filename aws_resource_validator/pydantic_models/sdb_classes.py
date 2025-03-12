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
from aws_resource_validator.pydantic_models.sdb_constants import *

class AttributeTypeDef(BaseValidatorModel):
    Name: str
    Value: str
    AlternateNameEncoding: Optional[str] = None
    AlternateValueEncoding: Optional[str] = None


class CreateDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str


class UpdateConditionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Exists: Optional[bool] = None


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DomainMetadataRequestTypeDef(BaseValidatorModel):
    DomainName: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetAttributesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ItemName: str
    AttributeNames: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDomainsRequestTypeDef(BaseValidatorModel):
    MaxNumberOfDomains: Optional[int] = None
    NextToken: Optional[str] = None


class ReplaceableAttributeTypeDef(BaseValidatorModel):
    Name: str
    Value: str
    Replace: Optional[bool] = None


class SelectRequestTypeDef(BaseValidatorModel):
    SelectExpression: str
    NextToken: Optional[str] = None
    ConsistentRead: Optional[bool] = None


class DeletableItemTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Optional[Sequence[AttributeTypeDef]] = None


class ItemTypeDef(BaseValidatorModel):
    Name: str
    Attributes: List[AttributeTypeDef]
    AlternateNameEncoding: Optional[str] = None


class DeleteAttributesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ItemName: str
    Attributes: Optional[Sequence[AttributeTypeDef]] = None
    Expected: Optional[UpdateConditionTypeDef] = None


class DomainMetadataResultTypeDef(BaseValidatorModel):
    ItemCount: int
    ItemNamesSizeBytes: int
    AttributeNameCount: int
    AttributeNamesSizeBytes: int
    AttributeValueCount: int
    AttributeValuesSizeBytes: int
    Timestamp: int
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAttributesResultTypeDef(BaseValidatorModel):
    Attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainsResultTypeDef(BaseValidatorModel):
    DomainNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDomainsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SelectRequestPaginateTypeDef(BaseValidatorModel):
    SelectExpression: str
    ConsistentRead: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PutAttributesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ItemName: str
    Attributes: Sequence[ReplaceableAttributeTypeDef]
    Expected: Optional[UpdateConditionTypeDef] = None


class ReplaceableItemTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Sequence[ReplaceableAttributeTypeDef]


class BatchDeleteAttributesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Items: Sequence[DeletableItemTypeDef]


class SelectResultTypeDef(BaseValidatorModel):
    Items: List[ItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchPutAttributesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Items: Sequence[ReplaceableItemTypeDef]


