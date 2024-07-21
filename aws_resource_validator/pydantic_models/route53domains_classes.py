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
from aws_resource_validator.pydantic_models.route53domains_constants import *

class AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef(BaseModel):
    DomainName: str
    Password: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DnssecSigningAttributesTypeDef(BaseModel):
    Algorithm: Optional[int] = None
    Flags: Optional[int] = None
    PublicKey: Optional[str] = None

class BillingRecordTypeDef(BaseModel):
    DomainName: Optional[str] = None
    Operation: Optional[OperationTypeType] = None
    InvoiceId: Optional[str] = None
    BillDate: Optional[datetime] = None
    Price: Optional[float] = None

class CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef(BaseModel):
    DomainName: str

class CheckDomainAvailabilityRequestRequestTypeDef(BaseModel):
    DomainName: str
    IdnLangCode: Optional[str] = None

class CheckDomainTransferabilityRequestRequestTypeDef(BaseModel):
    DomainName: str
    AuthCode: Optional[str] = None

class DomainTransferabilityTypeDef(BaseModel):
    Transferable: Optional[TransferableType] = None

class ConsentTypeDef(BaseModel):
    MaxPrice: float
    Currency: str

class ExtraParamTypeDef(BaseModel):
    Name: ExtraParamNameType
    Value: str

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DeleteTagsForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    TagsToDelete: Sequence[str]

class DisableDomainAutoRenewRequestRequestTypeDef(BaseModel):
    DomainName: str

class DisableDomainTransferLockRequestRequestTypeDef(BaseModel):
    DomainName: str

class DisassociateDelegationSignerFromDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    Id: str

class DnssecKeyTypeDef(BaseModel):
    Algorithm: Optional[int] = None
    Flags: Optional[int] = None
    PublicKey: Optional[str] = None
    DigestType: Optional[int] = None
    Digest: Optional[str] = None
    KeyTag: Optional[int] = None
    Id: Optional[str] = None

class PriceWithCurrencyTypeDef(BaseModel):
    Price: float
    Currency: str

class DomainSuggestionTypeDef(BaseModel):
    DomainName: Optional[str] = None
    Availability: Optional[str] = None

class DomainSummaryTypeDef(BaseModel):
    DomainName: Optional[str] = None
    AutoRenew: Optional[bool] = None
    TransferLock: Optional[bool] = None
    Expiry: Optional[datetime] = None

class EnableDomainAutoRenewRequestRequestTypeDef(BaseModel):
    DomainName: str

class EnableDomainTransferLockRequestRequestTypeDef(BaseModel):
    DomainName: str

class FilterConditionTypeDef(BaseModel):
    Name: ListDomainsAttributeNameType
    Operator: OperatorType
    Values: Sequence[str]

class GetContactReachabilityStatusRequestRequestTypeDef(BaseModel):
    domainName: Optional[str] = None

class GetDomainDetailRequestRequestTypeDef(BaseModel):
    DomainName: str

class NameserverOutputTypeDef(BaseModel):
    Name: str
    GlueIps: Optional[List[str]] = None

class GetDomainSuggestionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    SuggestionCount: int
    OnlyAvailable: bool

class GetOperationDetailRequestRequestTypeDef(BaseModel):
    OperationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SortConditionTypeDef(BaseModel):
    Name: ListDomainsAttributeNameType
    SortOrder: SortOrderType

class OperationSummaryTypeDef(BaseModel):
    OperationId: Optional[str] = None
    Status: Optional[OperationStatusType] = None
    Type: Optional[OperationTypeType] = None
    SubmittedDate: Optional[datetime] = None
    DomainName: Optional[str] = None
    Message: Optional[str] = None
    StatusFlag: Optional[StatusFlagType] = None
    LastUpdatedDate: Optional[datetime] = None

class ListPricesRequestRequestTypeDef(BaseModel):
    Tld: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListTagsForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class NameserverTypeDef(BaseModel):
    Name: str
    GlueIps: Optional[Sequence[str]] = None

class PushDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    Target: str

class RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef(BaseModel):
    DomainName: str

class RenewDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    CurrentExpiryYear: int
    DurationInYears: Optional[int] = None

class ResendContactReachabilityEmailRequestRequestTypeDef(BaseModel):
    domainName: Optional[str] = None

class ResendOperationAuthorizationRequestRequestTypeDef(BaseModel):
    OperationId: str

class RetrieveDomainAuthCodeRequestRequestTypeDef(BaseModel):
    DomainName: str

class TransferDomainToAnotherAwsAccountRequestRequestTypeDef(BaseModel):
    DomainName: str
    AccountId: str

class UpdateDomainContactPrivacyRequestRequestTypeDef(BaseModel):
    DomainName: str
    AdminPrivacy: Optional[bool] = None
    RegistrantPrivacy: Optional[bool] = None
    TechPrivacy: Optional[bool] = None
    BillingPrivacy: Optional[bool] = None

class AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDelegationSignerToDomainResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDomainTransferToAnotherAwsAccountResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDomainAvailabilityResponseTypeDef(BaseModel):
    Availability: DomainAvailabilityType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDomainTransferLockResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateDelegationSignerFromDomainResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDomainTransferLockResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactReachabilityStatusResponseTypeDef(BaseModel):
    domainName: str
    status: ReachabilityStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationDetailResponseTypeDef(BaseModel):
    OperationId: str
    Status: OperationStatusType
    Message: str
    DomainName: str
    Type: OperationTypeType
    SubmittedDate: datetime
    LastUpdatedDate: datetime
    StatusFlag: StatusFlagType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDomainResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectDomainTransferFromAnotherAwsAccountResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RenewDomainResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResendContactReachabilityEmailResponseTypeDef(BaseModel):
    domainName: str
    emailAddress: str
    isAlreadyVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveDomainAuthCodeResponseTypeDef(BaseModel):
    AuthCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainToAnotherAwsAccountResponseTypeDef(BaseModel):
    OperationId: str
    Password: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainContactPrivacyResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainContactResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameserversResponseTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDelegationSignerToDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    SigningAttributes: DnssecSigningAttributesTypeDef

class ViewBillingResponseTypeDef(BaseModel):
    NextPageMarker: str
    BillingRecords: List[BillingRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDomainTransferabilityResponseTypeDef(BaseModel):
    Transferability: DomainTransferabilityTypeDef
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContactDetailOutputTypeDef(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    ContactType: Optional[ContactTypeType] = None
    OrganizationName: Optional[str] = None
    AddressLine1: Optional[str] = None
    AddressLine2: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    CountryCode: Optional[CountryCodeType] = None
    ZipCode: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    Fax: Optional[str] = None
    ExtraParams: Optional[List[ExtraParamTypeDef]] = None

class ContactDetailTypeDef(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    ContactType: Optional[ContactTypeType] = None
    OrganizationName: Optional[str] = None
    AddressLine1: Optional[str] = None
    AddressLine2: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    CountryCode: Optional[CountryCodeType] = None
    ZipCode: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Email: Optional[str] = None
    Fax: Optional[str] = None
    ExtraParams: Optional[Sequence[ExtraParamTypeDef]] = None

class DomainPriceTypeDef(BaseModel):
    Name: Optional[str] = None
    RegistrationPrice: Optional[PriceWithCurrencyTypeDef] = None
    TransferPrice: Optional[PriceWithCurrencyTypeDef] = None
    RenewalPrice: Optional[PriceWithCurrencyTypeDef] = None
    ChangeOwnershipPrice: Optional[PriceWithCurrencyTypeDef] = None
    RestorationPrice: Optional[PriceWithCurrencyTypeDef] = None

class GetDomainSuggestionsResponseTypeDef(BaseModel):
    SuggestionsList: List[DomainSuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(BaseModel):
    Domains: List[DomainSummaryTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricesRequestListPricesPaginateTypeDef(BaseModel):
    Tld: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseModel):
    FilterConditions: Optional[Sequence[FilterConditionTypeDef]] = None
    SortCondition: Optional[SortConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    FilterConditions: Optional[Sequence[FilterConditionTypeDef]] = None
    SortCondition: Optional[SortConditionTypeDef] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListOperationsRequestListOperationsPaginateTypeDef(BaseModel):
    SubmittedSince: Optional[TimestampTypeDef] = None
    Status: Optional[Sequence[OperationStatusType]] = None
    Type: Optional[Sequence[OperationTypeType]] = None
    SortBy: Optional[Literal["SubmittedDate"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsRequestRequestTypeDef(BaseModel):
    SubmittedSince: Optional[TimestampTypeDef] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    Status: Optional[Sequence[OperationStatusType]] = None
    Type: Optional[Sequence[OperationTypeType]] = None
    SortBy: Optional[Literal["SubmittedDate"]] = None
    SortOrder: Optional[SortOrderType] = None

class ViewBillingRequestRequestTypeDef(BaseModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ViewBillingRequestViewBillingPaginateTypeDef(BaseModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsResponseTypeDef(BaseModel):
    Operations: List[OperationSummaryTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForDomainResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTagsForDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    TagsToUpdate: Optional[Sequence[TagTypeDef]] = None

class GetDomainDetailResponseTypeDef(BaseModel):
    DomainName: str
    Nameservers: List[NameserverOutputTypeDef]
    AutoRenew: bool
    AdminContact: ContactDetailOutputTypeDef
    RegistrantContact: ContactDetailOutputTypeDef
    TechContact: ContactDetailOutputTypeDef
    AdminPrivacy: bool
    RegistrantPrivacy: bool
    TechPrivacy: bool
    RegistrarName: str
    WhoIsServer: str
    RegistrarUrl: str
    AbuseContactEmail: str
    AbuseContactPhone: str
    RegistryDomainId: str
    CreationDate: datetime
    UpdatedDate: datetime
    ExpirationDate: datetime
    Reseller: str
    DnsSec: str
    StatusList: List[str]
    DnssecKeys: List[DnssecKeyTypeDef]
    BillingContact: ContactDetailOutputTypeDef
    BillingPrivacy: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    DurationInYears: int
    AdminContact: ContactDetailTypeDef
    RegistrantContact: ContactDetailTypeDef
    TechContact: ContactDetailTypeDef
    IdnLangCode: Optional[str] = None
    AutoRenew: Optional[bool] = None
    PrivacyProtectAdminContact: Optional[bool] = None
    PrivacyProtectRegistrantContact: Optional[bool] = None
    PrivacyProtectTechContact: Optional[bool] = None
    BillingContact: Optional[ContactDetailTypeDef] = None
    PrivacyProtectBillingContact: Optional[bool] = None

class UpdateDomainContactRequestRequestTypeDef(BaseModel):
    DomainName: str
    AdminContact: Optional[ContactDetailTypeDef] = None
    RegistrantContact: Optional[ContactDetailTypeDef] = None
    TechContact: Optional[ContactDetailTypeDef] = None
    Consent: Optional[ConsentTypeDef] = None
    BillingContact: Optional[ContactDetailTypeDef] = None

class ListPricesResponseTypeDef(BaseModel):
    Prices: List[DomainPriceTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    DurationInYears: int
    AdminContact: ContactDetailTypeDef
    RegistrantContact: ContactDetailTypeDef
    TechContact: ContactDetailTypeDef
    IdnLangCode: Optional[str] = None
    Nameservers: Optional[Sequence[NameserverUnionTypeDef]] = None
    AuthCode: Optional[str] = None
    AutoRenew: Optional[bool] = None
    PrivacyProtectAdminContact: Optional[bool] = None
    PrivacyProtectRegistrantContact: Optional[bool] = None
    PrivacyProtectTechContact: Optional[bool] = None
    BillingContact: Optional[ContactDetailTypeDef] = None
    PrivacyProtectBillingContact: Optional[bool] = None

class UpdateDomainNameserversRequestRequestTypeDef(BaseModel):
    DomainName: str
    Nameservers: Sequence[NameserverUnionTypeDef]
    FIAuthKey: Optional[str] = None

