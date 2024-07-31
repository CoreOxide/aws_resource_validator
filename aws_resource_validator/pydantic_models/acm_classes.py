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
from aws_resource_validator.pydantic_models.acm_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class CertificateOptionsTypeDef(BaseModel):
    CertificateTransparencyLoggingPreference: Optional[       CertificateTransparencyLoggingPreferenceType     ] = None

class ExtendedKeyUsageTypeDef(BaseModel):
    Name: Optional[ExtendedKeyUsageNameType] = None
    OID: Optional[str] = None

class KeyUsageTypeDef(BaseModel):
    Name: Optional[KeyUsageNameType] = None

class CertificateSummaryTypeDef(BaseModel):
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

class DeleteCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DomainValidationOptionTypeDef(BaseModel):
    DomainName: str
    ValidationDomain: str

class ResourceRecordTypeDef(BaseModel):
    Name: str
    Type: Literal["CNAME"]
    Value: str

class ExpiryEventsConfigurationTypeDef(BaseModel):
    DaysBeforeExpiry: Optional[int] = None

class FiltersTypeDef(BaseModel):
    extendedKeyUsage: Optional[Sequence[ExtendedKeyUsageNameType]] = None
    keyUsage: Optional[Sequence[KeyUsageNameType]] = None
    keyTypes: Optional[Sequence[KeyAlgorithmType]] = None

class GetCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str

class RenewCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str

class ResendValidationEmailRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    Domain: str
    ValidationDomain: str

class AddTagsToCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    Tags: Sequence[TagTypeDef]

class RemoveTagsFromCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    Tags: Sequence[TagTypeDef]

class ExportCertificateRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    Passphrase: BlobTypeDef

class ImportCertificateRequestRequestTypeDef(BaseModel):
    Certificate: BlobTypeDef
    PrivateKey: BlobTypeDef
    CertificateArn: Optional[str] = None
    CertificateChain: Optional[BlobTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateCertificateOptionsRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    Options: CertificateOptionsTypeDef

class DescribeCertificateRequestCertificateValidatedWaitTypeDef(BaseModel):
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportCertificateResponseTypeDef(BaseModel):
    Certificate: str
    CertificateChain: str
    PrivateKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateResponseTypeDef(BaseModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateResponseTypeDef(BaseModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificatesResponseTypeDef(BaseModel):
    CertificateSummaryList: List[CertificateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForCertificateResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RequestCertificateResponseTypeDef(BaseModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RequestCertificateRequestRequestTypeDef(BaseModel):
    DomainName: str
    ValidationMethod: Optional[ValidationMethodType] = None
    SubjectAlternativeNames: Optional[Sequence[str]] = None
    IdempotencyToken: Optional[str] = None
    DomainValidationOptions: Optional[Sequence[DomainValidationOptionTypeDef]] = None
    Options: Optional[CertificateOptionsTypeDef] = None
    CertificateAuthorityArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KeyAlgorithm: Optional[KeyAlgorithmType] = None

class DomainValidationTypeDef(BaseModel):
    DomainName: str
    ValidationEmails: Optional[List[str]] = None
    ValidationDomain: Optional[str] = None
    ValidationStatus: Optional[DomainStatusType] = None
    ResourceRecord: Optional[ResourceRecordTypeDef] = None
    ValidationMethod: Optional[ValidationMethodType] = None

class GetAccountConfigurationResponseTypeDef(BaseModel):
    ExpiryEvents: ExpiryEventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountConfigurationRequestRequestTypeDef(BaseModel):
    IdempotencyToken: str
    ExpiryEvents: Optional[ExpiryEventsConfigurationTypeDef] = None

class ListCertificatesRequestRequestTypeDef(BaseModel):
    CertificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    Includes: Optional[FiltersTypeDef] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None
    SortBy: Optional[Literal["CREATED_AT"]] = None
    SortOrder: Optional[SortOrderType] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseModel):
    CertificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    Includes: Optional[FiltersTypeDef] = None
    SortBy: Optional[Literal["CREATED_AT"]] = None
    SortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class RenewalSummaryTypeDef(BaseModel):
    RenewalStatus: RenewalStatusType
    DomainValidationOptions: List[DomainValidationTypeDef]
    UpdatedAt: datetime
    RenewalStatusReason: Optional[FailureReasonType] = None

class CertificateDetailTypeDef(BaseModel):
    CertificateArn: Optional[str] = None
    DomainName: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    DomainValidationOptions: Optional[List[DomainValidationTypeDef]] = None
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
    RenewalSummary: Optional[RenewalSummaryTypeDef] = None
    KeyUsages: Optional[List[KeyUsageTypeDef]] = None
    ExtendedKeyUsages: Optional[List[ExtendedKeyUsageTypeDef]] = None
    CertificateAuthorityArn: Optional[str] = None
    RenewalEligibility: Optional[RenewalEligibilityType] = None
    Options: Optional[CertificateOptionsTypeDef] = None

class DescribeCertificateResponseTypeDef(BaseModel):
    Certificate: CertificateDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

