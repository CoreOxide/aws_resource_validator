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

class Attribute(BaseValidatorModel):
    Name: str
    Value: str
    AlternateNameEncoding: Optional[str] = None
    AlternateValueEncoding: Optional[str] = None


class CreateDomainRequest(BaseValidatorModel):
    DomainName: str


class UpdateCondition(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Exists: Optional[bool] = None


class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


class DomainMetadataRequest(BaseValidatorModel):
    DomainName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetAttributesRequest(BaseValidatorModel):
    DomainName: str
    ItemName: str
    AttributeNames: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDomainsRequest(BaseValidatorModel):
    MaxNumberOfDomains: Optional[int] = None
    NextToken: Optional[str] = None


class ReplaceableAttribute(BaseValidatorModel):
    Name: str
    Value: str
    Replace: Optional[bool] = None


class SelectRequest(BaseValidatorModel):
    SelectExpression: str
    NextToken: Optional[str] = None
    ConsistentRead: Optional[bool] = None


class DeletableItem(BaseValidatorModel):
    Name: str
    Attributes: Optional[Sequence[Attribute]] = None


class Item(BaseValidatorModel):
    Name: str
    Attributes: List[Attribute]
    AlternateNameEncoding: Optional[str] = None


class DeleteAttributesRequest(BaseValidatorModel):
    DomainName: str
    ItemName: str
    Attributes: Optional[Sequence[Attribute]] = None
    Expected: Optional[UpdateCondition] = None


class DomainMetadataResult(BaseValidatorModel):
    ItemCount: int
    ItemNamesSizeBytes: int
    AttributeNameCount: int
    AttributeNamesSizeBytes: int
    AttributeValueCount: int
    AttributeValuesSizeBytes: int
    Timestamp: int
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAttributesResult(BaseValidatorModel):
    Attributes: List[Attribute]
    ResponseMetadata: ResponseMetadata


class ListDomainsResult(BaseValidatorModel):
    DomainNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class SelectRequestPaginate(BaseValidatorModel):
    SelectExpression: str
    ConsistentRead: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class PutAttributesRequest(BaseValidatorModel):
    DomainName: str
    ItemName: str
    Attributes: Sequence[ReplaceableAttribute]
    Expected: Optional[UpdateCondition] = None


class ReplaceableItem(BaseValidatorModel):
    Name: str
    Attributes: Sequence[ReplaceableAttribute]


class BatchDeleteAttributesRequest(BaseValidatorModel):
    DomainName: str
    Items: Sequence[DeletableItem]


class SelectResult(BaseValidatorModel):
    Items: List[Item]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchPutAttributesRequest(BaseValidatorModel):
    DomainName: str
    Items: Sequence[ReplaceableItem]


