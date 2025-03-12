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

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class CertificateOptionsTypeDef(BaseValidatorModel):
    CertificateTransparencyLoggingPreference: Optional[ CertificateTransparencyLoggingPreferenceType ] = None


class ExtendedKeyUsageTypeDef(BaseValidatorModel):
    Name: Optional[ExtendedKeyUsageNameType] = None
    OID: Optional[str] = None


class KeyUsageTypeDef(BaseValidatorModel):
    Name: Optional[KeyUsageNameType] = None


class DeleteCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str


class DescribeCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DomainValidationOptionTypeDef(BaseValidatorModel):
    DomainName: str
    ValidationDomain: str


class ExpiryEventsConfigurationTypeDef(BaseValidatorModel):
    DaysBeforeExpiry: Optional[int] = None


class FiltersTypeDef(BaseValidatorModel):
    extendedKeyUsage: Optional[Sequence[ExtendedKeyUsageNameType]] = None
    keyUsage: Optional[Sequence[KeyUsageNameType]] = None
    keyTypes: Optional[Sequence[KeyAlgorithmType]] = None


class GetCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str


class RenewCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str


class ResendValidationEmailRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    Domain: str
    ValidationDomain: str


class AddTagsToCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    Tags: Sequence[TagTypeDef]


class RemoveTagsFromCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    Tags: Sequence[TagTypeDef]


class BlobTypeDef(BaseValidatorModel):
    pass


class ExportCertificateRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    Passphrase: BlobTypeDef


class ImportCertificateRequestTypeDef(BaseValidatorModel):
    Certificate: BlobTypeDef
    PrivateKey: BlobTypeDef
    CertificateArn: Optional[str] = None
    CertificateChain: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateCertificateOptionsRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    Options: CertificateOptionsTypeDef


class DescribeCertificateRequestWaitTypeDef(BaseValidatorModel):
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExportCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    PrivateKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportCertificateResponseTypeDef(BaseValidatorModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CertificateSummaryTypeDef(BaseValidatorModel):
    pass


class ListCertificatesResponseTypeDef(BaseValidatorModel):
    CertificateSummaryList: List[CertificateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForCertificateResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RequestCertificateResponseTypeDef(BaseValidatorModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class RequestCertificateRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ValidationMethod: Optional[ValidationMethodType] = None
    SubjectAlternativeNames: Optional[Sequence[str]] = None
    IdempotencyToken: Optional[str] = None
    DomainValidationOptions: Optional[Sequence[DomainValidationOptionTypeDef]] = None
    Options: Optional[CertificateOptionsTypeDef] = None
    CertificateAuthorityArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KeyAlgorithm: Optional[KeyAlgorithmType] = None


class ResourceRecordTypeDef(BaseValidatorModel):
    pass


class DomainValidationTypeDef(BaseValidatorModel):
    DomainName: str
    ValidationEmails: Optional[List[str]] = None
    ValidationDomain: Optional[str] = None
    ValidationStatus: Optional[DomainStatusType] = None
    ResourceRecord: Optional[ResourceRecordTypeDef] = None
    ValidationMethod: Optional[ValidationMethodType] = None


class GetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    ExpiryEvents: ExpiryEventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutAccountConfigurationRequestTypeDef(BaseValidatorModel):
    IdempotencyToken: str
    ExpiryEvents: Optional[ExpiryEventsConfigurationTypeDef] = None


class ListCertificatesRequestTypeDef(BaseValidatorModel):
    CertificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    Includes: Optional[FiltersTypeDef] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None
    SortBy: Optional[Literal["CREATED_AT"]] = None
    SortOrder: Optional[SortOrderType] = None


class ListCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    CertificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    Includes: Optional[FiltersTypeDef] = None
    SortBy: Optional[Literal["CREATED_AT"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class RenewalSummaryTypeDef(BaseValidatorModel):
    RenewalStatus: RenewalStatusType
    DomainValidationOptions: List[DomainValidationTypeDef]
    UpdatedAt: datetime
    RenewalStatusReason: Optional[FailureReasonType] = None


class CertificateDetailTypeDef(BaseValidatorModel):
    pass


class DescribeCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: CertificateDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


