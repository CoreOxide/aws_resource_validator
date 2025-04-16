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
from aws_resource_validator.pydantic_models.acm_constants import *

class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class CertificateOptions(BaseValidatorModel):
    CertificateTransparencyLoggingPreference: Optional[ CertificateTransparencyLoggingPreferenceType ] = None


class ExtendedKeyUsage(BaseValidatorModel):
    Name: Optional[ExtendedKeyUsageNameType] = None
    OID: Optional[str] = None


class KeyUsage(BaseValidatorModel):
    Name: Optional[KeyUsageNameType] = None


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


class ExpiryEventsConfiguration(BaseValidatorModel):
    DaysBeforeExpiry: Optional[int] = None


class Filters(BaseValidatorModel):
    extendedKeyUsage: Optional[Sequence[ExtendedKeyUsageNameType]] = None
    keyUsage: Optional[Sequence[KeyUsageNameType]] = None
    keyTypes: Optional[Sequence[KeyAlgorithmType]] = None


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
    Tags: Sequence[Tag]


class RemoveTagsFromCertificateRequest(BaseValidatorModel):
    CertificateArn: str
    Tags: Sequence[Tag]


class Blob(BaseValidatorModel):
    pass


class ExportCertificateRequest(BaseValidatorModel):
    CertificateArn: str
    Passphrase: Blob


class ImportCertificateRequest(BaseValidatorModel):
    Certificate: Blob
    PrivateKey: Blob
    CertificateArn: Optional[str] = None
    CertificateChain: Optional[Blob] = None
    Tags: Optional[Sequence[Tag]] = None


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


class CertificateSummary(BaseValidatorModel):
    pass


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
    SubjectAlternativeNames: Optional[Sequence[str]] = None
    IdempotencyToken: Optional[str] = None
    DomainValidationOptions: Optional[Sequence[DomainValidationOption]] = None
    Options: Optional[CertificateOptions] = None
    CertificateAuthorityArn: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    KeyAlgorithm: Optional[KeyAlgorithmType] = None


class ResourceRecord(BaseValidatorModel):
    pass


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
    CertificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    Includes: Optional[Filters] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None
    SortBy: Optional[Literal["CREATED_AT"]] = None
    SortOrder: Optional[SortOrderType] = None


class ListCertificatesRequestPaginate(BaseValidatorModel):
    CertificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    Includes: Optional[Filters] = None
    SortBy: Optional[Literal["CREATED_AT"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class RenewalSummary(BaseValidatorModel):
    RenewalStatus: RenewalStatusType
    DomainValidationOptions: List[DomainValidation]
    UpdatedAt: datetime
    RenewalStatusReason: Optional[FailureReasonType] = None


class CertificateDetail(BaseValidatorModel):
    pass


class DescribeCertificateResponse(BaseValidatorModel):
    Certificate: CertificateDetail
    ResponseMetadata: ResponseMetadata


