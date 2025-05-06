from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.invoicing.invoicing_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BatchGetInvoiceProfileRequest(BaseValidatorModel):
    AccountIds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ResourceTag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteInvoiceUnitRequest(BaseValidatorModel):
    InvoiceUnitArn: str


class Filters(BaseValidatorModel):
    Names: Optional[List[str]] = None
    InvoiceReceivers: Optional[List[str]] = None
    Accounts: Optional[List[str]] = None

Timestamp = Union[datetime, str]


class InvoiceUnitRuleOutput(BaseValidatorModel):
    LinkedAccounts: Optional[List[str]] = None


class ReceiverAddress(BaseValidatorModel):
    AddressLine1: Optional[str] = None
    AddressLine2: Optional[str] = None
    AddressLine3: Optional[str] = None
    DistrictOrCounty: Optional[str] = None
    City: Optional[str] = None
    StateOrRegion: Optional[str] = None
    CountryCode: Optional[str] = None
    CompanyName: Optional[str] = None
    PostalCode: Optional[str] = None


class InvoiceUnitRule(BaseValidatorModel):
    LinkedAccounts: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: List[str]


class CreateInvoiceUnitResponse(BaseValidatorModel):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadata


class DeleteInvoiceUnitResponse(BaseValidatorModel):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadata


class UpdateInvoiceUnitResponse(BaseValidatorModel):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: List[ResourceTag]


class GetInvoiceUnitRequest(BaseValidatorModel):
    InvoiceUnitArn: str
    AsOf: Optional[Timestamp] = None


class ListInvoiceUnitsRequest(BaseValidatorModel):
    Filters: Optional[Filters] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AsOf: Optional[Timestamp] = None


class GetInvoiceUnitResponse(BaseValidatorModel):
    InvoiceUnitArn: str
    InvoiceReceiver: str
    Name: str
    Description: str
    TaxInheritanceDisabled: bool
    Rule: InvoiceUnitRuleOutput
    LastModified: datetime
    ResponseMetadata: ResponseMetadata


class InvoiceUnit(BaseValidatorModel):
    InvoiceUnitArn: Optional[str] = None
    InvoiceReceiver: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    TaxInheritanceDisabled: Optional[bool] = None
    Rule: Optional[InvoiceUnitRuleOutput] = None
    LastModified: Optional[datetime] = None


class InvoiceProfile(BaseValidatorModel):
    AccountId: Optional[str] = None
    ReceiverName: Optional[str] = None
    ReceiverAddress: Optional[ReceiverAddress] = None
    ReceiverEmail: Optional[str] = None
    Issuer: Optional[str] = None
    TaxRegistrationNumber: Optional[str] = None

InvoiceUnitRuleUnion = Union[InvoiceUnitRule, InvoiceUnitRuleOutput]


class ListInvoiceUnitsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Filters] = None
    AsOf: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvoiceUnitsResponse(BaseValidatorModel):
    InvoiceUnits: List[InvoiceUnit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetInvoiceProfileResponse(BaseValidatorModel):
    Profiles: List[InvoiceProfile]
    ResponseMetadata: ResponseMetadata


class CreateInvoiceUnitRequest(BaseValidatorModel):
    Name: str
    InvoiceReceiver: str
    Rule: InvoiceUnitRuleUnion
    Description: Optional[str] = None
    TaxInheritanceDisabled: Optional[bool] = None
    ResourceTags: Optional[List[ResourceTag]] = None


class UpdateInvoiceUnitRequest(BaseValidatorModel):
    InvoiceUnitArn: str
    Description: Optional[str] = None
    TaxInheritanceDisabled: Optional[bool] = None
    Rule: Optional[InvoiceUnitRuleUnion] = None