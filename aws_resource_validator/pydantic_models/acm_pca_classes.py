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
from aws_resource_validator.pydantic_models.acm_pca_constants import *

class CustomAttributeTypeDef(BaseValidatorModel):
    ObjectIdentifier: str
    Value: str


class AccessMethodTypeDef(BaseValidatorModel):
    CustomObjectIdentifier: Optional[str] = None
    AccessMethodType: Optional[AccessMethodTypeType] = None


class CreateCertificateAuthorityAuditReportRequestTypeDef(BaseValidatorModel):
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


class CreatePermissionRequestTypeDef(BaseValidatorModel):
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


class DeleteCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    PermanentDeletionTimeInDays: Optional[int] = None


class DeletePermissionRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Principal: str
    SourceAccount: Optional[str] = None


class DeletePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DescribeCertificateAuthorityAuditReportRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    AuditReportId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeCertificateAuthorityRequestTypeDef(BaseValidatorModel):
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


class GetCertificateAuthorityCertificateRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str


class GetCertificateAuthorityCsrRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str


class GetCertificateRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateArn: str


class GetPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCertificateAuthoritiesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceOwner: Optional[ResourceOwnerType] = None


class ListPermissionsRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PermissionTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Principal: Optional[str] = None
    SourceAccount: Optional[str] = None
    Actions: Optional[List[ActionTypeType]] = None
    Policy: Optional[str] = None


class ListTagsRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OcspConfigurationTypeDef(BaseValidatorModel):
    Enabled: bool
    OcspCustomCname: Optional[str] = None


class QualifierTypeDef(BaseValidatorModel):
    CpsUri: str


class PutPolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RestoreCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str


class RevokeCertificateRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateSerial: str
    RevocationReason: RevocationReasonType


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


class BlobTypeDef(BaseValidatorModel):
    pass


class ImportCertificateAuthorityCertificateRequestTypeDef(BaseValidatorModel):
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


class TagCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]


class UntagCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: Sequence[TagTypeDef]


class CrlConfigurationTypeDef(BaseValidatorModel):
    Enabled: bool
    ExpirationInDays: Optional[int] = None
    CustomCname: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3ObjectAcl: Optional[S3ObjectAclType] = None
    CrlDistributionPointExtensionConfiguration: Optional[ CrlDistributionPointExtensionConfigurationTypeDef ] = None
    CrlType: Optional[CrlTypeType] = None
    CustomPath: Optional[str] = None


class DescribeCertificateAuthorityAuditReportRequestWaitTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    AuditReportId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetCertificateAuthorityCsrRequestWaitTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetCertificateRequestWaitTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class ListCertificateAuthoritiesRequestPaginateTypeDef(BaseValidatorModel):
    ResourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionsRequestPaginateTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsRequestPaginateTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionsResponseTypeDef(BaseValidatorModel):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PolicyQualifierInfoTypeDef(BaseValidatorModel):
    PolicyQualifierId: Literal["CPS"]
    Qualifier: QualifierTypeDef


class GeneralNameOutputTypeDef(BaseValidatorModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectOutputTypeDef] = None
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


class AccessDescriptionOutputTypeDef(BaseValidatorModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameOutputTypeDef


class ASN1SubjectUnionTypeDef(BaseValidatorModel):
    pass


class GeneralNameTypeDef(BaseValidatorModel):
    OtherName: Optional[OtherNameTypeDef] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectUnionTypeDef] = None
    EdiPartyName: Optional[EdiPartyNameTypeDef] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None


class UpdateCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    Status: Optional[CertificateAuthorityStatusType] = None


class CsrExtensionsOutputTypeDef(BaseValidatorModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[List[AccessDescriptionOutputTypeDef]] = None


class AccessDescriptionTypeDef(BaseValidatorModel):
    AccessMethod: AccessMethodTypeDef
    AccessLocation: GeneralNameTypeDef


class CertificateAuthorityConfigurationOutputTypeDef(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectOutputTypeDef
    CsrExtensions: Optional[CsrExtensionsOutputTypeDef] = None


class CsrExtensionsTypeDef(BaseValidatorModel):
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectInformationAccess: Optional[Sequence[AccessDescriptionTypeDef]] = None


class GeneralNameUnionTypeDef(BaseValidatorModel):
    pass


class ExtensionsTypeDef(BaseValidatorModel):
    CertificatePolicies: Optional[Sequence[PolicyInformationTypeDef]] = None
    ExtendedKeyUsage: Optional[Sequence[ExtendedKeyUsageTypeDef]] = None
    KeyUsage: Optional[KeyUsageTypeDef] = None
    SubjectAlternativeNames: Optional[Sequence[GeneralNameUnionTypeDef]] = None
    CustomExtensions: Optional[Sequence[CustomExtensionTypeDef]] = None


class CertificateAuthorityConfigurationTypeDef(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectTypeDef
    CsrExtensions: Optional[CsrExtensionsTypeDef] = None


class ApiPassthroughTypeDef(BaseValidatorModel):
    Extensions: Optional[ExtensionsTypeDef] = None
    Subject: Optional[ASN1SubjectUnionTypeDef] = None


class CertificateAuthorityTypeDef(BaseValidatorModel):
    pass


class DescribeCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    CertificateAuthority: CertificateAuthorityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCertificateAuthoritiesResponseTypeDef(BaseValidatorModel):
    CertificateAuthorities: List[CertificateAuthorityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ValidityTypeDef(BaseValidatorModel):
    pass


class IssueCertificateRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    Csr: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmType
    Validity: ValidityTypeDef
    ApiPassthrough: Optional[ApiPassthroughTypeDef] = None
    TemplateArn: Optional[str] = None
    ValidityNotBefore: Optional[ValidityTypeDef] = None
    IdempotencyToken: Optional[str] = None


class CertificateAuthorityConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityConfiguration: CertificateAuthorityConfigurationUnionTypeDef
    CertificateAuthorityType: CertificateAuthorityTypeType
    RevocationConfiguration: Optional[RevocationConfigurationTypeDef] = None
    IdempotencyToken: Optional[str] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None


