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
from aws_resource_validator.pydantic_models.acm_pca_constants import *

class CustomAttributeTypeDef(BaseValidatorModel):
    ObjectIdentifier: str
    Value: str

class AccessMethodTypeDef(BaseValidatorModel):
    CustomObjectIdentifier: Optional[str] = None
    AccessMethodType: Optional[AccessMethodTypeType] = None

class CreateCertificateAuthorityAuditReportRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    S3BucketName: str
    AuditReportResponseFormat: AuditReportResponseFormatType

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class CreatePermissionRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Principal: str
    Actions: Sequence[ActionTypeType]
    SourceAccount: Optional[str] = None

class CrlDistributionPointExtensionConfigurationTypeDef(BaseValidatorModel):
    OmitExtension: bool

class KeyUsageTypeDef(BaseValidatorModel):
    DigitalSignature: Optional[bool] = None
    NonRepudiation: Optional[bool] = None
    KeyEncipherment: Optional[bool] = None
    DataEncipherment: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    KeyCertSign: Optional[bool] = None
    CRLSign: Optional[bool] = None
    EncipherOnly: Optional[bool] = None
    DecipherOnly: Optional[bool] = None

class CustomExtensionTypeDef(BaseValidatorModel):
    ObjectIdentifier: str
    Value: str
    Critical: Optional[bool] = None

class DeleteCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    PermanentDeletionTimeInDays: Optional[int] = None

class DeletePermissionRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Principal: str
    SourceAccount: Optional[str] = None

class DeletePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeCertificateAuthorityAuditReportRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    AuditReportId: str

class DescribeCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str

class EdiPartyNameTypeDef(BaseValidatorModel):
    PartyName: str
    NameAssigner: Optional[str] = None

class ExtendedKeyUsageTypeDef(BaseValidatorModel):
    ExtendedKeyUsageType: Optional[ExtendedKeyUsageTypeType] = None
    ExtendedKeyUsageObjectIdentifier: Optional[str] = None

class OtherNameTypeDef(BaseValidatorModel):
    TypeId: str
    Value: str

class GetCertificateAuthorityCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str

class GetCertificateAuthorityCsrRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str

class GetCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateArn: str

class GetPolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ValidityTypeDef(BaseValidatorModel):
    Value: int
    Type: ValidityPeriodTypeType

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCertificateAuthoritiesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceOwner: Optional[ResourceOwnerType] = None

class ListPermissionsRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PermissionTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Principal: Optional[str] = None
    SourceAccount: Optional[str] = None
    Actions: Optional[List[ActionTypeType]] = None
    Policy: Optional[str] = None

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OcspConfigurationTypeDef(BaseValidatorModel):
    Enabled: bool
    OcspCustomCname: Optional[str] = None

class QualifierTypeDef(BaseValidatorModel):
    CpsUri: str

class PutPolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str

class RestoreCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str

class RevokeCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateSerial: str
    RevocationReason: RevocationReasonType

class ASN1SubjectExtraOutputTypeDef(BaseValidatorModel):
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

class ASN1SubjectOutputTypeDef(BaseValidatorModel):
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

class ASN1SubjectTypeDef(BaseValidatorModel):
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

class ImportCertificateAuthorityCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Certificate: BlobTypeDef
    CertificateChain: Optional[BlobTypeDef] = None

class CreateCertificateAuthorityAuditReportResponseTypeDef(BaseValidatorModel):
    AuditReportId: str
    S3Key: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateAuthorityAuditReportResponseTypeDef(BaseValidatorModel):
    AuditReportStatus: AuditReportStatusType
    S3BucketName: str
    S3Key: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateAuthorityCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateAuthorityCsrResponseTypeDef(BaseValidatorModel):
    Csr: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class IssueCertificateResponseTypeDef(BaseValidatorModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]

class UntagCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]

class CrlConfigurationTypeDef(BaseValidatorModel):
    Enabled: bool
    ExpirationInDays: Optional[int] = None
    CustomCname: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3ObjectAcl: Optional[S3ObjectAclType] = None
    CrlDistributionPointExtensionConfiguration: Optional[       CrlDistributionPointExtensionConfigurationTypeDef     ] = None

class DescribeCertificateAuthorityAuditReportRequestAuditReportCreatedWaitTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    AuditReportId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetCertificateAuthorityCsrRequestCertificateAuthorityCSRCreatedWaitTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetCertificateRequestCertificateIssuedWaitTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListCertificateAuthoritiesRequestListCertificateAuthoritiesPaginateTypeDef(BaseValidatorModel):
    ResourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionsRequestListPermissionsPaginateTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionsResponseTypeDef(BaseValidatorModel):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PolicyQualifierInfoTypeDef(BaseValidatorModel):
    PolicyQualifierId: Literal["CPS"]
    Qualifier: QualifierTypeDef

class GeneralNameExtraOutputTypeDef(BaseValidatorModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectExtraOutputTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None

class GeneralNameOutputTypeDef(BaseValidatorModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectOutputTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None

class GeneralNameTypeDef(BaseValidatorModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None

class RevocationConfigurationTypeDef(BaseValidatorModel):
    CrlConfiguration: Optional[CrlConfigurationTypeDef] = None
    OcspConfiguration: Optional[OcspConfigurationTypeDef] = None

class PolicyInformationTypeDef(BaseValidatorModel):
    CertPolicyId: str
    PolicyQualifiers: Optional[Sequence[PolicyQualifierInfoTypeDef]] = None

class AccessDescriptionExtraOutputTypeDef(BaseValidatorModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameExtraOutputTypeDef

class AccessDescriptionOutputTypeDef(BaseValidatorModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameOutputTypeDef

class AccessDescriptionTypeDef(BaseValidatorModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameTypeDef

class UpdateCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    Status: Optional[CertificateAuthorityStatusType] = None

class ExtensionsTypeDef(BaseValidatorModel):
    CertificatePolicies: Optional[Sequence[PolicyInformationTypeDef]] = None
    ExtendedKeyUsage: Optional[Sequence[ExtendedKeyUsageTypeDef]] = None
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectAlternativeNames: Optional[Sequence[GeneralNameTypeDef]] = None
    CustomExtensions: Optional[Sequence[CustomExtensionTypeDef]] = None

class CsrExtensionsExtraOutputTypeDef(BaseValidatorModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[List[AccessDescriptionExtraOutputTypeDef]] = None

class CsrExtensionsOutputTypeDef(BaseValidatorModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[List[AccessDescriptionOutputTypeDef]] = None

class CsrExtensionsTypeDef(BaseValidatorModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[Sequence[AccessDescriptionTypeDef]] = None

class ApiPassthroughTypeDef(BaseValidatorModel):
    Extensions: Optional[ExtensionsTypeDef] = None
    Subject: Optional[ASN1SubjectTypeDef] = None

class CertificateAuthorityConfigurationExtraOutputTypeDef(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectExtraOutputTypeDef
    CsrExtensions: Optional[CsrExtensionsExtraOutputTypeDef] = None

class CertificateAuthorityConfigurationOutputTypeDef(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectOutputTypeDef
    CsrExtensions: Optional[CsrExtensionsOutputTypeDef] = None

class CertificateAuthorityConfigurationTypeDef(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectTypeDef
    CsrExtensions: Optional[CsrExtensionsTypeDef] = None

class IssueCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Csr: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmType
    Validity: ValidityTypeDef
    ApiPassthrough: Optional[ApiPassthroughTypeDef] = None
    TemplateArn: Optional[str] = None
    ValidityNotBefore: Optional[ValidityTypeDef] = None
    IdempotencyToken: Optional[str] = None

class CertificateAuthorityTypeDef(BaseValidatorModel):
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

class CreateCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityConfiguration: CertificateAuthorityConfigurationTypeDef
    CertificateAuthorityType: CertificateAuthorityTypeType
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    IdempotencyToken: Optional[str] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None

class DescribeCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    CertificateAuthority: CertificateAuthorityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificateAuthoritiesResponseTypeDef(BaseValidatorModel):
    CertificateAuthorities: List[CertificateAuthorityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

