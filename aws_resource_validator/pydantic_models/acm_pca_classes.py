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
from aws_resource_validator.pydantic_models.acm_pca_constants import *

class CustomAttributeTypeDef(BaseModel):
    ObjectIdentifier: str
    Value: str

class AccessMethodTypeDef(BaseModel):
    CustomObjectIdentifier: Optional[str] = None
    AccessMethodType: Optional[AccessMethodTypeType] = None

class CreateCertificateAuthorityAuditReportRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    S3BucketName: str
    AuditReportResponseFormat: AuditReportResponseFormatType

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class CreatePermissionRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    Principal: str
    Actions: Sequence[ActionTypeType]
    SourceAccount: Optional[str] = None

class CrlDistributionPointExtensionConfigurationTypeDef(BaseModel):
    OmitExtension: bool

class KeyUsageTypeDef(BaseModel):
    DigitalSignature: Optional[bool] = None
    NonRepudiation: Optional[bool] = None
    KeyEncipherment: Optional[bool] = None
    DataEncipherment: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    KeyCertSign: Optional[bool] = None
    CRLSign: Optional[bool] = None
    EncipherOnly: Optional[bool] = None
    DecipherOnly: Optional[bool] = None

class CustomExtensionTypeDef(BaseModel):
    ObjectIdentifier: str
    Value: str
    Critical: Optional[bool] = None

class DeleteCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    PermanentDeletionTimeInDays: Optional[int] = None

class DeletePermissionRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    Principal: str
    SourceAccount: Optional[str] = None

class DeletePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeCertificateAuthorityAuditReportRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    AuditReportId: str

class DescribeCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str

class EdiPartyNameTypeDef(BaseModel):
    PartyName: str
    NameAssigner: Optional[str] = None

class ExtendedKeyUsageTypeDef(BaseModel):
    ExtendedKeyUsageType: Optional[ExtendedKeyUsageTypeType] = None
    ExtendedKeyUsageObjectIdentifier: Optional[str] = None

class OtherNameTypeDef(BaseModel):
    TypeId: str
    Value: str

class GetCertificateAuthorityCertificateRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str

class GetCertificateAuthorityCsrRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str

class GetCertificateRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    CertificateArn: str

class GetPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ValidityTypeDef(BaseModel):
    Value: int
    Type: ValidityPeriodTypeType

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCertificateAuthoritiesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceOwner: Optional[ResourceOwnerType] = None

class ListPermissionsRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PermissionTypeDef(BaseModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Principal: Optional[str] = None
    SourceAccount: Optional[str] = None
    Actions: Optional[List[ActionTypeType]] = None
    Policy: Optional[str] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OcspConfigurationTypeDef(BaseModel):
    Enabled: bool
    OcspCustomCname: Optional[str] = None

class QualifierTypeDef(BaseModel):
    CpsUri: str

class PutPolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str

class RestoreCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str

class RevokeCertificateRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    CertificateSerial: str
    RevocationReason: RevocationReasonType

class ASN1SubjectExtraOutputTypeDef(BaseModel):
    Country: Optional[str] = None
    Organization: Optional[str] = None
    OrganizationalUnit: Optional[str] = None
    DistinguishedNameQualifier: Optional[str] = None
    State: Optional[str] = None
    CommonName: Optional[str] = None
    SerialNumber: Optional[str] = None
    Locality: Optional[str] = None
    Title: Optional[str] = None
    Surname: Optional[str] = None
    GivenName: Optional[str] = None
    Initials: Optional[str] = None
    Pseudonym: Optional[str] = None
    GenerationQualifier: Optional[str] = None
    CustomAttributes: Optional[List[CustomAttributeTypeDef]] = None

class ASN1SubjectOutputTypeDef(BaseModel):
    Country: Optional[str] = None
    Organization: Optional[str] = None
    OrganizationalUnit: Optional[str] = None
    DistinguishedNameQualifier: Optional[str] = None
    State: Optional[str] = None
    CommonName: Optional[str] = None
    SerialNumber: Optional[str] = None
    Locality: Optional[str] = None
    Title: Optional[str] = None
    Surname: Optional[str] = None
    GivenName: Optional[str] = None
    Initials: Optional[str] = None
    Pseudonym: Optional[str] = None
    GenerationQualifier: Optional[str] = None
    CustomAttributes: Optional[List[CustomAttributeTypeDef]] = None

class ASN1SubjectTypeDef(BaseModel):
    Country: Optional[str] = None
    Organization: Optional[str] = None
    OrganizationalUnit: Optional[str] = None
    DistinguishedNameQualifier: Optional[str] = None
    State: Optional[str] = None
    CommonName: Optional[str] = None
    SerialNumber: Optional[str] = None
    Locality: Optional[str] = None
    Title: Optional[str] = None
    Surname: Optional[str] = None
    GivenName: Optional[str] = None
    Initials: Optional[str] = None
    Pseudonym: Optional[str] = None
    GenerationQualifier: Optional[str] = None
    CustomAttributes: Optional[Sequence[CustomAttributeTypeDef]] = None

class ImportCertificateAuthorityCertificateRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    Certificate: BlobTypeDef
    CertificateChain: Optional[BlobTypeDef] = None

class CreateCertificateAuthorityAuditReportResponseTypeDef(BaseModel):
    AuditReportId: str
    S3Key: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCertificateAuthorityResponseTypeDef(BaseModel):
    CertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateAuthorityAuditReportResponseTypeDef(BaseModel):
    AuditReportStatus: AuditReportStatusType
    S3BucketName: str
    S3Key: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateAuthorityCertificateResponseTypeDef(BaseModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateAuthorityCsrResponseTypeDef(BaseModel):
    Csr: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateResponseTypeDef(BaseModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class IssueCertificateResponseTypeDef(BaseModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]

class UntagCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]

class CrlConfigurationTypeDef(BaseModel):
    Enabled: bool
    ExpirationInDays: Optional[int] = None
    CustomCname: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3ObjectAcl: Optional[S3ObjectAclType] = None
    CrlDistributionPointExtensionConfiguration: Optional[       CrlDistributionPointExtensionConfigurationTypeDef     ] = None

class DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef(BaseModel):
    CertificateAuthorityArn: str
    AuditReportId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef(BaseModel):
    CertificateAuthorityArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetCertificateRequestCertificateIssuedWaitTypeDef(BaseModel):
    CertificateAuthorityArn: str
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef(BaseModel):
    ResourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionsRequestListPermissionsPaginateTypeDef(BaseModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionsResponseTypeDef(BaseModel):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PolicyQualifierInfoTypeDef(BaseModel):
    PolicyQualifierId: Literal["CPS"]
    Qualifier: QualifierTypeDef

class GeneralNameExtraOutputTypeDef(BaseModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectExtraOutputTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None

class GeneralNameOutputTypeDef(BaseModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectOutputTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None

class GeneralNameTypeDef(BaseModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None

class RevocationConfigurationTypeDef(BaseModel):
    CrlConfiguration: Optional[CrlConfigurationTypeDef] = None
    OcspConfiguration: Optional[OcspConfigurationTypeDef] = None

class PolicyInformationTypeDef(BaseModel):
    CertPolicyId: str
    PolicyQualifiers: Optional[Sequence[PolicyQualifierInfoTypeDef]] = None

class AccessDescriptionExtraOutputTypeDef(BaseModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameExtraOutputTypeDef

class AccessDescriptionOutputTypeDef(BaseModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameOutputTypeDef

class AccessDescriptionTypeDef(BaseModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameTypeDef

class UpdateCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    Status: Optional[CertificateAuthorityStatusType] = None

class ExtensionsTypeDef(BaseModel):
    CertificatePolicies: Optional[Sequence[PolicyInformationTypeDef]] = None
    ExtendedKeyUsage: Optional[Sequence[ExtendedKeyUsageTypeDef]] = None
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectAlternativeNames: Optional[Sequence[GeneralNameTypeDef]] = None
    CustomExtensions: Optional[Sequence[CustomExtensionTypeDef]] = None

class CsrExtensionsExtraOutputTypeDef(BaseModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[List[AccessDescriptionExtraOutputTypeDef]] = None

class CsrExtensionsOutputTypeDef(BaseModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[List[AccessDescriptionOutputTypeDef]] = None

class CsrExtensionsTypeDef(BaseModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[Sequence[AccessDescriptionTypeDef]] = None

class ApiPassthroughTypeDef(BaseModel):
    Extensions: Optional[ExtensionsTypeDef] = None
    Subject: Optional[ASN1SubjectTypeDef] = None

class CertificateAuthorityConfigurationExtraOutputTypeDef(BaseModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectExtraOutputTypeDef
    CsrExtensions: Optional[CsrExtensionsExtraOutputTypeDef] = None

class CertificateAuthorityConfigurationOutputTypeDef(BaseModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectOutputTypeDef
    CsrExtensions: Optional[CsrExtensionsOutputTypeDef] = None

class CertificateAuthorityConfigurationTypeDef(BaseModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectTypeDef
    CsrExtensions: Optional[CsrExtensionsTypeDef] = None

class IssueCertificateRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    Csr: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmType
    Validity: ValidityTypeDef
    ApiPassthrough: Optional[ApiPassthroughTypeDef] = None
    TemplateArn: Optional[str] = None
    ValidityNotBefore: Optional[ValidityTypeDef] = None
    IdempotencyToken: Optional[str] = None

class CertificateAuthorityTypeDef(BaseModel):
    Arn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastStateChangeAt: Optional[datetime] = None
    Type: Optional[CertificateAuthorityTypeType] = None
    Serial: Optional[str] = None
    Status: Optional[CertificateAuthorityStatusType] = None
    NotBefore: Optional[datetime] = None
    NotAfter: Optional[datetime] = None
    FailureReason: Optional[FailureReasonType] = None
    CertificateAuthorityConfiguration: Optional[       CertificateAuthorityConfigurationOutputTypeDef     ] = None
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    RestorableUntil: Optional[datetime] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None

class CreateCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityConfiguration: CertificateAuthorityConfigurationTypeDef
    CertificateAuthorityType: CertificateAuthorityTypeType
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    IdempotencyToken: Optional[str] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None

class DescribeCertificateAuthorityResponseTypeDef(BaseModel):
    CertificateAuthority: CertificateAuthorityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificateAuthoritiesResponseTypeDef(BaseModel):
    CertificateAuthorities: List[CertificateAuthorityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

