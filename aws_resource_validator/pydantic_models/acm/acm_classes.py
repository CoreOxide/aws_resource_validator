from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.acm.acm_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CertificateOptions(BaseValidatorModel):
    CertificateTransparencyLoggingPreference: Optional[CertificateTransparencyLoggingPreferenceType] = None


class ExtendedKeyUsage(BaseValidatorModel):
    Name: Optional[ExtendedKeyUsageNameType] = None
    OID: Optional[str] = None


class KeyUsage(BaseValidatorModel):
    Name: Optional[KeyUsageNameType] = None


class CertificateSummary(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DomainName: Optional[str] = None
    SubjectAlternativeNameSummaries: Optional[List[str]] = None
    HasAdditionalSubjectAlternativeNames: Optional[bool] = None
    Status: Optional[CertificateStatusType] = None
    Type: Optional[CertificateTypeType] = None
    KeyAlgorithm: Optional[KeyAlgorithmType] = None
    KeyUsages: Optional[List[KeyUsageNameType]] = None
    ExtendedKeyUsages: Optional[List[ExtendedKeyUsageNameType]] = None
    InUse: Optional[bool] = None
    Exported: Optional[bool] = None
    RenewalEligibility: Optional[RenewalEligibilityType] = None
    NotBefore: Optional[datetime] = None
    NotAfter: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    IssuedAt: Optional[datetime] = None
    ImportedAt: Optional[datetime] = None
    RevokedAt: Optional[datetime] = None


class DeleteCertificateRequest(BaseValidatorModel):
    CertificateArn: str


class DescribeCertificateRequest(BaseValidatorModel):
    CertificateArn: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DomainValidationOption(BaseValidatorModel):
    DomainName: str
    ValidationDomain: str


class ResourceRecord(BaseValidatorModel):
    Name: str
    Type: Literal['CNAME']
    Value: str


class ExpiryEventsConfiguration(BaseValidatorModel):
    DaysBeforeExpiry: Optional[int] = None


class Filters(BaseValidatorModel):
    extendedKeyUsage: Optional[List[ExtendedKeyUsageNameType]] = None
    keyUsage: Optional[List[KeyUsageNameType]] = None
    keyTypes: Optional[List[KeyAlgorithmType]] = None


class GetCertificateRequest(BaseValidatorModel):
    CertificateArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForCertificateRequest(BaseValidatorModel):
    CertificateArn: str


class RenewCertificateRequest(BaseValidatorModel):
    CertificateArn: str


class ResendValidationEmailRequest(BaseValidatorModel):
    CertificateArn: str
    Domain: str
    ValidationDomain: str


class AddTagsToCertificateRequest(BaseValidatorModel):
    CertificateArn: str
    Tags: List[Tag]


class RemoveTagsFromCertificateRequest(BaseValidatorModel):
    CertificateArn: str
    Tags: List[Tag]


class ExportCertificateRequest(BaseValidatorModel):
    CertificateArn: str
    Passphrase: Blob


class ImportCertificateRequest(BaseValidatorModel):
    Certificate: Blob
    PrivateKey: Blob
    CertificateArn: Optional[str] = None
    CertificateChain: Optional[Blob] = None
    Tags: Optional[List[Tag]] = None


class UpdateCertificateOptionsRequest(BaseValidatorModel):
    CertificateArn: str
    Options: CertificateOptions


class DescribeCertificateRequestWait(BaseValidatorModel):
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExportCertificateResponse(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    PrivateKey: str
    ResponseMetadata: ResponseMetadata


class GetCertificateResponse(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadata


class ImportCertificateResponse(BaseValidatorModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadata


class ListCertificatesResponse(BaseValidatorModel):
    CertificateSummaryList: List[CertificateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForCertificateResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class RequestCertificateResponse(BaseValidatorModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadata


class RequestCertificateRequest(BaseValidatorModel):
    DomainName: str
    ValidationMethod: Optional[ValidationMethodType] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    IdempotencyToken: Optional[str] = None
    DomainValidationOptions: Optional[List[DomainValidationOption]] = None
    Options: Optional[CertificateOptions] = None
    CertificateAuthorityArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    KeyAlgorithm: Optional[KeyAlgorithmType] = None


class DomainValidation(BaseValidatorModel):
    DomainName: str
    ValidationEmails: Optional[List[str]] = None
    ValidationDomain: Optional[str] = None
    ValidationStatus: Optional[DomainStatusType] = None
    ResourceRecord: Optional[ResourceRecord] = None
    ValidationMethod: Optional[ValidationMethodType] = None


class GetAccountConfigurationResponse(BaseValidatorModel):
    ExpiryEvents: ExpiryEventsConfiguration
    ResponseMetadata: ResponseMetadata


class PutAccountConfigurationRequest(BaseValidatorModel):
    IdempotencyToken: str
    ExpiryEvents: Optional[ExpiryEventsConfiguration] = None


class ListCertificatesRequest(BaseValidatorModel):
    CertificateStatuses: Optional[List[CertificateStatusType]] = None
    Includes: Optional[Filters] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None
    SortBy: Optional[Literal['CREATED_AT']] = None
    SortOrder: Optional[SortOrderType] = None


class ListCertificatesRequestPaginate(BaseValidatorModel):
    CertificateStatuses: Optional[List[CertificateStatusType]] = None
    Includes: Optional[Filters] = None
    SortBy: Optional[Literal['CREATED_AT']] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class RenewalSummary(BaseValidatorModel):
    RenewalStatus: RenewalStatusType
    DomainValidationOptions: List[DomainValidation]
    UpdatedAt: datetime
    RenewalStatusReason: Optional[FailureReasonType] = None


class CertificateDetail(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DomainName: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    DomainValidationOptions: Optional[List[DomainValidation]] = None
    Serial: Optional[str] = None
    Subject: Optional[str] = None
    Issuer: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    IssuedAt: Optional[datetime] = None
    ImportedAt: Optional[datetime] = None
    Status: Optional[CertificateStatusType] = None
    RevokedAt: Optional[datetime] = None
    RevocationReason: Optional[RevocationReasonType] = None
    NotBefore: Optional[datetime] = None
    NotAfter: Optional[datetime] = None
    KeyAlgorithm: Optional[KeyAlgorithmType] = None
    SignatureAlgorithm: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    FailureReason: Optional[FailureReasonType] = None
    Type: Optional[CertificateTypeType] = None
    RenewalSummary: Optional[RenewalSummary] = None
    KeyUsages: Optional[List[KeyUsage]] = None
    ExtendedKeyUsages: Optional[List[ExtendedKeyUsage]] = None
    CertificateAuthorityArn: Optional[str] = None
    RenewalEligibility: Optional[RenewalEligibilityType] = None
    Options: Optional[CertificateOptions] = None


class DescribeCertificateResponse(BaseValidatorModel):
    Certificate: CertificateDetail
    ResponseMetadata: ResponseMetadata