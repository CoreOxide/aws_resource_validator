from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Password: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DnssecSigningAttributesTypeDef(BaseValidatorModel):
    Algorithm: Optional[int] = None
    Flags: Optional[int] = None
    PublicKey: Optional[str] = None

class BillingRecordTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    Operation: Optional[OperationTypeType] = None
    InvoiceId: Optional[str] = None
    BillDate: Optional[datetime] = None
    Price: Optional[float] = None

class CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class CheckDomainAvailabilityRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    IdnLangCode: Optional[str] = None

class CheckDomainTransferabilityRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AuthCode: Optional[str] = None

class DomainTransferabilityTypeDef(BaseValidatorModel):
    Transferable: Optional[TransferableType] = None

class ConsentTypeDef(BaseValidatorModel):
    MaxPrice: float
    Currency: str

class ExtraParamTypeDef(BaseValidatorModel):
    Name: ExtraParamNameType
    Value: str

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DeleteTagsForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    TagsToDelete: Sequence[str]

class DisableDomainAutoRenewRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DisableDomainTransferLockRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DisassociateDelegationSignerFromDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Id: str

class DnssecKeyTypeDef(BaseValidatorModel):
    Algorithm: Optional[int] = None
    Flags: Optional[int] = None
    PublicKey: Optional[str] = None
    DigestType: Optional[int] = None
    Digest: Optional[str] = None
    KeyTag: Optional[int] = None
    Id: Optional[str] = None

class PriceWithCurrencyTypeDef(BaseValidatorModel):
    Price: float
    Currency: str

class DomainSuggestionTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    Availability: Optional[str] = None

class DomainSummaryTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    AutoRenew: Optional[bool] = None
    TransferLock: Optional[bool] = None
    Expiry: Optional[datetime] = None

class EnableDomainAutoRenewRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class EnableDomainTransferLockRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class FilterConditionTypeDef(BaseValidatorModel):
    Name: ListDomainsAttributeNameType
    Operator: OperatorType
    Values: Sequence[str]

class GetContactReachabilityStatusRequestRequestTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None

class GetDomainDetailRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class NameserverOutputTypeDef(BaseValidatorModel):
    Name: str
    GlueIps: Optional[List[str]] = None

class GetDomainSuggestionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SuggestionCount: int
    OnlyAvailable: bool

class GetOperationDetailRequestRequestTypeDef(BaseValidatorModel):
    OperationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SortConditionTypeDef(BaseValidatorModel):
    Name: ListDomainsAttributeNameType
    SortOrder: SortOrderType

class OperationSummaryTypeDef(BaseValidatorModel):
    OperationId: Optional[str] = None
    Status: Optional[OperationStatusType] = None
    Type: Optional[OperationTypeType] = None
    SubmittedDate: Optional[datetime] = None
    DomainName: Optional[str] = None
    Message: Optional[str] = None
    StatusFlag: Optional[StatusFlagType] = None
    LastUpdatedDate: Optional[datetime] = None

class ListPricesRequestRequestTypeDef(BaseValidatorModel):
    Tld: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListTagsForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class NameserverTypeDef(BaseValidatorModel):
    Name: str
    GlueIps: Optional[Sequence[str]] = None

class PushDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Target: str

class RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class RenewDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CurrentExpiryYear: int
    DurationInYears: Optional[int] = None

class ResendContactReachabilityEmailRequestRequestTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None

class ResendOperationAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    OperationId: str

class RetrieveDomainAuthCodeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class TransferDomainToAnotherAwsAccountRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AccountId: str

class UpdateDomainContactPrivacyRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AdminPrivacy: Optional[bool] = None
    RegistrantPrivacy: Optional[bool] = None
    TechPrivacy: Optional[bool] = None
    BillingPrivacy: Optional[bool] = None

class AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDelegationSignerToDomainResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDomainTransferToAnotherAwsAccountResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDomainAvailabilityResponseTypeDef(BaseValidatorModel):
    Availability: DomainAvailabilityType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDomainTransferLockResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateDelegationSignerFromDomainResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDomainTransferLockResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactReachabilityStatusResponseTypeDef(BaseValidatorModel):
    domainName: str
    status: ReachabilityStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationDetailResponseTypeDef(BaseValidatorModel):
    OperationId: str
    Status: OperationStatusType
    Message: str
    DomainName: str
    Type: OperationTypeType
    SubmittedDate: datetime
    LastUpdatedDate: datetime
    StatusFlag: StatusFlagType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDomainResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectDomainTransferFromAnotherAwsAccountResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RenewDomainResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResendContactReachabilityEmailResponseTypeDef(BaseValidatorModel):
    domainName: str
    emailAddress: str
    isAlreadyVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveDomainAuthCodeResponseTypeDef(BaseValidatorModel):
    AuthCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainToAnotherAwsAccountResponseTypeDef(BaseValidatorModel):
    OperationId: str
    Password: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainContactPrivacyResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainContactResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameserversResponseTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDelegationSignerToDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SigningAttributes: DnssecSigningAttributesTypeDef

class ViewBillingResponseTypeDef(BaseValidatorModel):
    NextPageMarker: str
    BillingRecords: List[BillingRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDomainTransferabilityResponseTypeDef(BaseValidatorModel):
    Transferability: DomainTransferabilityTypeDef
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContactDetailOutputTypeDef(BaseValidatorModel):
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

class ContactDetailTypeDef(BaseValidatorModel):
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

class DomainPriceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    RegistrationPrice: Optional[PriceWithCurrencyTypeDef] = None
    TransferPrice: Optional[PriceWithCurrencyTypeDef] = None
    RenewalPrice: Optional[PriceWithCurrencyTypeDef] = None
    ChangeOwnershipPrice: Optional[PriceWithCurrencyTypeDef] = None
    RestorationPrice: Optional[PriceWithCurrencyTypeDef] = None

class GetDomainSuggestionsResponseTypeDef(BaseValidatorModel):
    SuggestionsList: List[DomainSuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(BaseValidatorModel):
    Domains: List[DomainSummaryTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricesRequestListPricesPaginateTypeDef(BaseValidatorModel):
    Tld: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseValidatorModel):
    FilterConditions: Optional[Sequence[FilterConditionTypeDef]] = None
    SortCondition: Optional[SortConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    FilterConditions: Optional[Sequence[FilterConditionTypeDef]] = None
    SortCondition: Optional[SortConditionTypeDef] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListOperationsRequestListOperationsPaginateTypeDef(BaseValidatorModel):
    SubmittedSince: Optional[TimestampTypeDef] = None
    Status: Optional[Sequence[OperationStatusType]] = None
    Type: Optional[Sequence[OperationTypeType]] = None
    SortBy: Optional[Literal["SubmittedDate"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsRequestRequestTypeDef(BaseValidatorModel):
    SubmittedSince: Optional[TimestampTypeDef] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    Status: Optional[Sequence[OperationStatusType]] = None
    Type: Optional[Sequence[OperationTypeType]] = None
    SortBy: Optional[Literal["SubmittedDate"]] = None
    SortOrder: Optional[SortOrderType] = None

class ViewBillingRequestRequestTypeDef(BaseValidatorModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ViewBillingRequestViewBillingPaginateTypeDef(BaseValidatorModel):
    Start: Optional[TimestampTypeDef] = None
    End: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsResponseTypeDef(BaseValidatorModel):
    Operations: List[OperationSummaryTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForDomainResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTagsForDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    TagsToUpdate: Optional[Sequence[TagTypeDef]] = None

class GetDomainDetailResponseTypeDef(BaseValidatorModel):
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

class RegisterDomainRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDomainContactRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AdminContact: Optional[ContactDetailTypeDef] = None
    RegistrantContact: Optional[ContactDetailTypeDef] = None
    TechContact: Optional[ContactDetailTypeDef] = None
    Consent: Optional[ConsentTypeDef] = None
    BillingContact: Optional[ContactDetailTypeDef] = None

class ListPricesResponseTypeDef(BaseValidatorModel):
    Prices: List[DomainPriceTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDomainNameserversRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Nameservers: Sequence[NameserverUnionTypeDef]
    FIAuthKey: Optional[str] = None

