from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53domains.route53domains_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_domain_transfer_from_another_aws_account' function.
class AcceptDomainTransferFromAnotherAwsAccountRequest(BaseValidatorModel):
    DomainName: str
    Password: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DnssecSigningAttributes(BaseValidatorModel):
    Algorithm: Optional[int] = None
    Flags: Optional[int] = None
    PublicKey: Optional[str] = None


class BillingRecord(BaseValidatorModel):
    DomainName: Optional[str] = None
    Operation: Optional[OperationTypeType] = None
    InvoiceId: Optional[str] = None
    BillDate: Optional[datetime] = None
    Price: Optional[float] = None


# This class is the input for the 'cancel_domain_transfer_to_another_aws_account' function.
class CancelDomainTransferToAnotherAwsAccountRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'check_domain_availability' function.
class CheckDomainAvailabilityRequest(BaseValidatorModel):
    DomainName: str
    IdnLangCode: Optional[str] = None


# This class is the input for the 'check_domain_transferability' function.
class CheckDomainTransferabilityRequest(BaseValidatorModel):
    DomainName: str
    AuthCode: Optional[str] = None


class DomainTransferability(BaseValidatorModel):
    Transferable: Optional[TransferableType] = None


class Consent(BaseValidatorModel):
    MaxPrice: float
    Currency: str


class ExtraParam(BaseValidatorModel):
    Name: ExtraParamNameType
    Value: str


# This class is the input for the 'delete_domain' function.
class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


class DeleteTagsForDomainRequest(BaseValidatorModel):
    DomainName: str
    TagsToDelete: List[str]


class DisableDomainAutoRenewRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'disable_domain_transfer_lock' function.
class DisableDomainTransferLockRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'disassociate_delegation_signer_from_domain' function.
class DisassociateDelegationSignerFromDomainRequest(BaseValidatorModel):
    DomainName: str
    Id: str


class DnssecKey(BaseValidatorModel):
    Algorithm: Optional[int] = None
    Flags: Optional[int] = None
    PublicKey: Optional[str] = None
    DigestType: Optional[int] = None
    Digest: Optional[str] = None
    KeyTag: Optional[int] = None
    Id: Optional[str] = None


class PriceWithCurrency(BaseValidatorModel):
    Price: float
    Currency: str


class DomainSuggestion(BaseValidatorModel):
    DomainName: Optional[str] = None
    Availability: Optional[str] = None


class DomainSummary(BaseValidatorModel):
    DomainName: Optional[str] = None
    AutoRenew: Optional[bool] = None
    TransferLock: Optional[bool] = None
    Expiry: Optional[datetime] = None


class EnableDomainAutoRenewRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'enable_domain_transfer_lock' function.
class EnableDomainTransferLockRequest(BaseValidatorModel):
    DomainName: str


class FilterCondition(BaseValidatorModel):
    Name: ListDomainsAttributeNameType
    Operator: OperatorType
    Values: List[str]


# This class is the input for the 'get_contact_reachability_status' function.
class GetContactReachabilityStatusRequest(BaseValidatorModel):
    domainName: Optional[str] = None


# This class is the input for the 'get_domain_detail' function.
class GetDomainDetailRequest(BaseValidatorModel):
    DomainName: str


class NameserverOutput(BaseValidatorModel):
    Name: str
    GlueIps: Optional[List[str]] = None


# This class is the input for the 'get_domain_suggestions' function.
class GetDomainSuggestionsRequest(BaseValidatorModel):
    DomainName: str
    SuggestionCount: int
    OnlyAvailable: bool


# This class is the input for the 'get_operation_detail' function.
class GetOperationDetailRequest(BaseValidatorModel):
    OperationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class SortCondition(BaseValidatorModel):
    Name: ListDomainsAttributeNameType
    SortOrder: SortOrderType

Timestamp = Union[datetime, str]


class OperationSummary(BaseValidatorModel):
    OperationId: Optional[str] = None
    Status: Optional[OperationStatusType] = None
    Type: Optional[OperationTypeType] = None
    SubmittedDate: Optional[datetime] = None
    DomainName: Optional[str] = None
    Message: Optional[str] = None
    StatusFlag: Optional[StatusFlagType] = None
    LastUpdatedDate: Optional[datetime] = None


# This class is the input for the 'list_prices' function.
class ListPricesRequest(BaseValidatorModel):
    Tld: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the input for the 'list_tags_for_domain' function.
class ListTagsForDomainRequest(BaseValidatorModel):
    DomainName: str


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class Nameserver(BaseValidatorModel):
    Name: str
    GlueIps: Optional[List[str]] = None


# This class is the input for the 'push_domain' function.
class PushDomainRequest(BaseValidatorModel):
    DomainName: str
    Target: str


# This class is the input for the 'reject_domain_transfer_from_another_aws_account' function.
class RejectDomainTransferFromAnotherAwsAccountRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'renew_domain' function.
class RenewDomainRequest(BaseValidatorModel):
    DomainName: str
    CurrentExpiryYear: int
    DurationInYears: Optional[int] = None


# This class is the input for the 'resend_contact_reachability_email' function.
class ResendContactReachabilityEmailRequest(BaseValidatorModel):
    domainName: Optional[str] = None


# This class is the input for the 'resend_operation_authorization' function.
class ResendOperationAuthorizationRequest(BaseValidatorModel):
    OperationId: str


# This class is the input for the 'retrieve_domain_auth_code' function.
class RetrieveDomainAuthCodeRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'transfer_domain_to_another_aws_account' function.
class TransferDomainToAnotherAwsAccountRequest(BaseValidatorModel):
    DomainName: str
    AccountId: str


# This class is the input for the 'update_domain_contact_privacy' function.
class UpdateDomainContactPrivacyRequest(BaseValidatorModel):
    DomainName: str
    AdminPrivacy: Optional[bool] = None
    RegistrantPrivacy: Optional[bool] = None
    TechPrivacy: Optional[bool] = None
    BillingPrivacy: Optional[bool] = None


# This class is the output for the 'accept_domain_transfer_from_another_aws_account' function.
class AcceptDomainTransferFromAnotherAwsAccountResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_delegation_signer_to_domain' function.
class AssociateDelegationSignerToDomainResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_domain_transfer_to_another_aws_account' function.
class CancelDomainTransferToAnotherAwsAccountResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'check_domain_availability' function.
class CheckDomainAvailabilityResponse(BaseValidatorModel):
    Availability: DomainAvailabilityType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain' function.
class DeleteDomainResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_domain_transfer_lock' function.
class DisableDomainTransferLockResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_delegation_signer_from_domain' function.
class DisassociateDelegationSignerFromDomainResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resend_operation_authorization' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_domain_transfer_lock' function.
class EnableDomainTransferLockResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_contact_reachability_status' function.
class GetContactReachabilityStatusResponse(BaseValidatorModel):
    domainName: str
    status: ReachabilityStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_operation_detail' function.
class GetOperationDetailResponse(BaseValidatorModel):
    OperationId: str
    Status: OperationStatusType
    Message: str
    DomainName: str
    Type: OperationTypeType
    SubmittedDate: datetime
    LastUpdatedDate: datetime
    StatusFlag: StatusFlagType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_domain' function.
class RegisterDomainResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_domain_transfer_from_another_aws_account' function.
class RejectDomainTransferFromAnotherAwsAccountResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'renew_domain' function.
class RenewDomainResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resend_contact_reachability_email' function.
class ResendContactReachabilityEmailResponse(BaseValidatorModel):
    domainName: str
    emailAddress: str
    isAlreadyVerified: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'retrieve_domain_auth_code' function.
class RetrieveDomainAuthCodeResponse(BaseValidatorModel):
    AuthCode: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'transfer_domain' function.
class TransferDomainResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'transfer_domain_to_another_aws_account' function.
class TransferDomainToAnotherAwsAccountResponse(BaseValidatorModel):
    OperationId: str
    Password: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_contact_privacy' function.
class UpdateDomainContactPrivacyResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_contact' function.
class UpdateDomainContactResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_nameservers' function.
class UpdateDomainNameserversResponse(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_delegation_signer_to_domain' function.
class AssociateDelegationSignerToDomainRequest(BaseValidatorModel):
    DomainName: str
    SigningAttributes: DnssecSigningAttributes


# This class is the output for the 'view_billing' function.
class ViewBillingResponse(BaseValidatorModel):
    NextPageMarker: str
    BillingRecords: List[BillingRecord]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'check_domain_transferability' function.
class CheckDomainTransferabilityResponse(BaseValidatorModel):
    Transferability: DomainTransferability
    Message: str
    ResponseMetadata: ResponseMetadata


class ContactDetailOutput(BaseValidatorModel):
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
    ExtraParams: Optional[List[ExtraParam]] = None


class ContactDetail(BaseValidatorModel):
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
    ExtraParams: Optional[List[ExtraParam]] = None


class DomainPrice(BaseValidatorModel):
    Name: Optional[str] = None
    RegistrationPrice: Optional[PriceWithCurrency] = None
    TransferPrice: Optional[PriceWithCurrency] = None
    RenewalPrice: Optional[PriceWithCurrency] = None
    ChangeOwnershipPrice: Optional[PriceWithCurrency] = None
    RestorationPrice: Optional[PriceWithCurrency] = None


# This class is the output for the 'get_domain_suggestions' function.
class GetDomainSuggestionsResponse(BaseValidatorModel):
    SuggestionsList: List[DomainSuggestion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_domains' function.
class ListDomainsResponse(BaseValidatorModel):
    Domains: List[DomainSummary]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadata


class ListPricesRequestPaginate(BaseValidatorModel):
    Tld: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    FilterConditions: Optional[List[FilterCondition]] = None
    SortCondition: Optional[SortCondition] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_domains' function.
class ListDomainsRequest(BaseValidatorModel):
    FilterConditions: Optional[List[FilterCondition]] = None
    SortCondition: Optional[SortCondition] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListOperationsRequestPaginate(BaseValidatorModel):
    SubmittedSince: Optional[Timestamp] = None
    Status: Optional[List[OperationStatusType]] = None
    Type: Optional[List[OperationTypeType]] = None
    SortBy: Optional[Literal['SubmittedDate']] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_operations' function.
class ListOperationsRequest(BaseValidatorModel):
    SubmittedSince: Optional[Timestamp] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    Status: Optional[List[OperationStatusType]] = None
    Type: Optional[List[OperationTypeType]] = None
    SortBy: Optional[Literal['SubmittedDate']] = None
    SortOrder: Optional[SortOrderType] = None


class ViewBillingRequestPaginate(BaseValidatorModel):
    Start: Optional[Timestamp] = None
    End: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'view_billing' function.
class ViewBillingRequest(BaseValidatorModel):
    Start: Optional[Timestamp] = None
    End: Optional[Timestamp] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


# This class is the output for the 'list_operations' function.
class ListOperationsResponse(BaseValidatorModel):
    Operations: List[OperationSummary]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_domain' function.
class ListTagsForDomainResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateTagsForDomainRequest(BaseValidatorModel):
    DomainName: str
    TagsToUpdate: Optional[List[Tag]] = None

NameserverUnion = Union[Nameserver, NameserverOutput]


# This class is the output for the 'get_domain_detail' function.
class GetDomainDetailResponse(BaseValidatorModel):
    DomainName: str
    Nameservers: List[NameserverOutput]
    AutoRenew: bool
    AdminContact: ContactDetailOutput
    RegistrantContact: ContactDetailOutput
    TechContact: ContactDetailOutput
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
    DnssecKeys: List[DnssecKey]
    BillingContact: ContactDetailOutput
    BillingPrivacy: bool
    ResponseMetadata: ResponseMetadata

ContactDetailUnion = Union[ContactDetail, ContactDetailOutput]


# This class is the output for the 'list_prices' function.
class ListPricesResponse(BaseValidatorModel):
    Prices: List[DomainPrice]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_domain_nameservers' function.
class UpdateDomainNameserversRequest(BaseValidatorModel):
    DomainName: str
    Nameservers: List[NameserverUnion]
    FIAuthKey: Optional[str] = None


# This class is the input for the 'register_domain' function.
class RegisterDomainRequest(BaseValidatorModel):
    DomainName: str
    DurationInYears: int
    AdminContact: ContactDetailUnion
    RegistrantContact: ContactDetailUnion
    TechContact: ContactDetailUnion
    IdnLangCode: Optional[str] = None
    AutoRenew: Optional[bool] = None
    PrivacyProtectAdminContact: Optional[bool] = None
    PrivacyProtectRegistrantContact: Optional[bool] = None
    PrivacyProtectTechContact: Optional[bool] = None
    BillingContact: Optional[ContactDetailUnion] = None
    PrivacyProtectBillingContact: Optional[bool] = None


# This class is the input for the 'transfer_domain' function.
class TransferDomainRequest(BaseValidatorModel):
    DomainName: str
    DurationInYears: int
    AdminContact: ContactDetailUnion
    RegistrantContact: ContactDetailUnion
    TechContact: ContactDetailUnion
    IdnLangCode: Optional[str] = None
    Nameservers: Optional[List[NameserverUnion]] = None
    AuthCode: Optional[str] = None
    AutoRenew: Optional[bool] = None
    PrivacyProtectAdminContact: Optional[bool] = None
    PrivacyProtectRegistrantContact: Optional[bool] = None
    PrivacyProtectTechContact: Optional[bool] = None
    BillingContact: Optional[ContactDetailUnion] = None
    PrivacyProtectBillingContact: Optional[bool] = None


# This class is the input for the 'update_domain_contact' function.
class UpdateDomainContactRequest(BaseValidatorModel):
    DomainName: str
    AdminContact: Optional[ContactDetailUnion] = None
    RegistrantContact: Optional[ContactDetailUnion] = None
    TechContact: Optional[ContactDetailUnion] = None
    Consent: Optional[Consent] = None
    BillingContact: Optional[ContactDetailUnion] = None