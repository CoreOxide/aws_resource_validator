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
from aws_resource_validator.pydantic_models.invoicing_constants import *

class BatchGetInvoiceProfileRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ResourceTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DeleteInvoiceUnitRequestTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str


class FiltersTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    InvoiceReceivers: Optional[Sequence[str]] = None
    Accounts: Optional[Sequence[str]] = None


class InvoiceUnitRuleOutputTypeDef(BaseValidatorModel):
    LinkedAccounts: Optional[List[str]] = None


class ReceiverAddressTypeDef(BaseValidatorModel):
    AddressLine1: Optional[str] = None
    AddressLine2: Optional[str] = None
    AddressLine3: Optional[str] = None
    DistrictOrCounty: Optional[str] = None
    City: Optional[str] = None
    StateOrRegion: Optional[str] = None
    CountryCode: Optional[str] = None
    CompanyName: Optional[str] = None
    PostalCode: Optional[str] = None


class InvoiceUnitRuleTypeDef(BaseValidatorModel):
    LinkedAccounts: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]


class CreateInvoiceUnitResponseTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInvoiceUnitResponseTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateInvoiceUnitResponseTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetInvoiceUnitRequestTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str
    AsOf: Optional[TimestampTypeDef] = None


class ListInvoiceUnitsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[FiltersTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AsOf: Optional[TimestampTypeDef] = None


class GetInvoiceUnitResponseTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str
    InvoiceReceiver: str
    Name: str
    Description: str
    TaxInheritanceDisabled: bool
    Rule: InvoiceUnitRuleOutputTypeDef
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class InvoiceUnitTypeDef(BaseValidatorModel):
    InvoiceUnitArn: Optional[str] = None
    InvoiceReceiver: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    TaxInheritanceDisabled: Optional[bool] = None
    Rule: Optional[InvoiceUnitRuleOutputTypeDef] = None
    LastModified: Optional[datetime] = None


class InvoiceProfileTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    ReceiverName: Optional[str] = None
    ReceiverAddress: Optional[ReceiverAddressTypeDef] = None
    ReceiverEmail: Optional[str] = None
    Issuer: Optional[str] = None
    TaxRegistrationNumber: Optional[str] = None


class ListInvoiceUnitsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[FiltersTypeDef] = None
    AsOf: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInvoiceUnitsResponseTypeDef(BaseValidatorModel):
    InvoiceUnits: List[InvoiceUnitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchGetInvoiceProfileResponseTypeDef(BaseValidatorModel):
    Profiles: List[InvoiceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InvoiceUnitRuleUnionTypeDef(BaseValidatorModel):
    pass


class CreateInvoiceUnitRequestTypeDef(BaseValidatorModel):
    Name: str
    InvoiceReceiver: str
    Rule: InvoiceUnitRuleUnionTypeDef
    Description: Optional[str] = None
    TaxInheritanceDisabled: Optional[bool] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class UpdateInvoiceUnitRequestTypeDef(BaseValidatorModel):
    InvoiceUnitArn: str
    Description: Optional[str] = None
    TaxInheritanceDisabled: Optional[bool] = None
    Rule: Optional[InvoiceUnitRuleUnionTypeDef] = None


