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

class CustomAttribute(BaseValidatorModel):
    ObjectIdentifier: str
    Value: str


class AccessMethod(BaseValidatorModel):
    CustomObjectIdentifier: Optional[str] = None
    AccessMethodType: Optional[AccessMethodTypeType] = None


class CreateCertificateAuthorityAuditReportRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    S3BucketName: str
    AuditReportResponseFormat: AuditReportResponseFormatType


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class CreatePermissionRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Principal: str
    Actions: Sequence[ActionTypeType]
    SourceAccount: Optional[str] = None


class CrlDistributionPointExtensionConfiguration(BaseValidatorModel):
    OmitExtension: bool


class KeyUsage(BaseValidatorModel):
    DigitalSignature: Optional[bool] = None
    NonRepudiation: Optional[bool] = None
    KeyEncipherment: Optional[bool] = None
    DataEncipherment: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    KeyCertSign: Optional[bool] = None
    CRLSign: Optional[bool] = None
    EncipherOnly: Optional[bool] = None
    DecipherOnly: Optional[bool] = None


class CustomExtension(BaseValidatorModel):
    ObjectIdentifier: str
    Value: str
    Critical: Optional[bool] = None


class DeleteCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    PermanentDeletionTimeInDays: Optional[int] = None


class DeletePermissionRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Principal: str
    SourceAccount: Optional[str] = None


class DeletePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DescribeCertificateAuthorityAuditReportRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    AuditReportId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str


class EdiPartyName(BaseValidatorModel):
    PartyName: str
    NameAssigner: Optional[str] = None


class ExtendedKeyUsage(BaseValidatorModel):
    ExtendedKeyUsageType: Optional[ExtendedKeyUsageTypeType] = None
    ExtendedKeyUsageObjectIdentifier: Optional[str] = None


class OtherName(BaseValidatorModel):
    TypeId: str
    Value: str


class GetCertificateAuthorityCertificateRequest(BaseValidatorModel):
    CertificateAuthorityArn: str


class GetCertificateAuthorityCsrRequest(BaseValidatorModel):
    CertificateAuthorityArn: str


class GetCertificateRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateArn: str


class GetPolicyRequest(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCertificateAuthoritiesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceOwner: Optional[ResourceOwnerType] = None


class ListPermissionsRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Permission(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Principal: Optional[str] = None
    SourceAccount: Optional[str] = None
    Actions: Optional[List[ActionTypeType]] = None
    Policy: Optional[str] = None


class ListTagsRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OcspConfiguration(BaseValidatorModel):
    Enabled: bool
    OcspCustomCname: Optional[str] = None


class Qualifier(BaseValidatorModel):
    CpsUri: str


class PutPolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class RestoreCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str


class RevokeCertificateRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateSerial: str
    RevocationReason: RevocationReasonType


class ASN1SubjectOutput(BaseValidatorModel):
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
    CustomAttributes: Optional[List[CustomAttribute]] = None


class ASN1Subject(BaseValidatorModel):
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
    CustomAttributes: Optional[Sequence[CustomAttribute]] = None


class Blob(BaseValidatorModel):
    pass


class ImportCertificateAuthorityCertificateRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Certificate: Blob
    CertificateChain: Optional[Blob] = None


class CreateCertificateAuthorityAuditReportResponse(BaseValidatorModel):
    AuditReportId: str
    S3Key: str
    ResponseMetadata: ResponseMetadata


class CreateCertificateAuthorityResponse(BaseValidatorModel):
    CertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadata


class DescribeCertificateAuthorityAuditReportResponse(BaseValidatorModel):
    AuditReportStatus: AuditReportStatusType
    S3BucketName: str
    S3Key: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCertificateAuthorityCertificateResponse(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadata


class GetCertificateAuthorityCsrResponse(BaseValidatorModel):
    Csr: str
    ResponseMetadata: ResponseMetadata


class GetCertificateResponse(BaseValidatorModel):
    Certificate: str
    CertificateChain: str
    ResponseMetadata: ResponseMetadata


class GetPolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class IssueCertificateResponse(BaseValidatorModel):
    CertificateArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: Sequence[Tag]


class UntagCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: Sequence[Tag]


class CrlConfiguration(BaseValidatorModel):
    Enabled: bool
    ExpirationInDays: Optional[int] = None
    CustomCname: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3ObjectAcl: Optional[S3ObjectAclType] = None
    CrlDistributionPointExtensionConfiguration: Optional[ CrlDistributionPointExtensionConfiguration ] = None
    CrlType: Optional[CrlTypeType] = None
    CustomPath: Optional[str] = None


class DescribeCertificateAuthorityAuditReportRequestWait(BaseValidatorModel):
    CertificateAuthorityArn: str
    AuditReportId: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetCertificateAuthorityCsrRequestWait(BaseValidatorModel):
    CertificateAuthorityArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetCertificateRequestWait(BaseValidatorModel):
    CertificateAuthorityArn: str
    CertificateArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListCertificateAuthoritiesRequestPaginate(BaseValidatorModel):
    ResourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPermissionsRequestPaginate(BaseValidatorModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsRequestPaginate(BaseValidatorModel):
    CertificateAuthorityArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPermissionsResponse(BaseValidatorModel):
    Permissions: List[Permission]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PolicyQualifierInfo(BaseValidatorModel):
    PolicyQualifierId: Literal["CPS"]
    Qualifier: Qualifier


class GeneralNameOutput(BaseValidatorModel):
    OtherName: Optional[OtherName] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectOutput] = None
    EdiPartyName: Optional[EdiPartyName] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None


class RevocationConfiguration(BaseValidatorModel):
    CrlConfiguration: Optional[CrlConfiguration] = None
    OcspConfiguration: Optional[OcspConfiguration] = None


class PolicyInformation(BaseValidatorModel):
    CertPolicyId: str
    PolicyQualifiers: Optional[Sequence[PolicyQualifierInfo]] = None


class AccessDescriptionOutput(BaseValidatorModel):
    AccessMethod: AccessMethod
    AccessLocation: GeneralNameOutput


class ASN1SubjectUnion(BaseValidatorModel):
    pass


class GeneralName(BaseValidatorModel):
    OtherName: Optional[OtherName] = None
    Rfc822Name: Optional[str] = None
    DnsName: Optional[str] = None
    DirectoryName: Optional[ASN1SubjectUnion] = None
    EdiPartyName: Optional[EdiPartyName] = None
    UniformResourceIdentifier: Optional[str] = None
    IpAddress: Optional[str] = None
    RegisteredId: Optional[str] = None


class UpdateCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    Status: Optional[CertificateAuthorityStatusType] = None


class CsrExtensionsOutput(BaseValidatorModel):
    KeyUsage: Optional[KeyUsage] = None
    SubjectInformationAccess: Optional[List[AccessDescriptionOutput]] = None


class AccessDescription(BaseValidatorModel):
    AccessMethod: AccessMethod
    AccessLocation: GeneralName


class CertificateAuthorityConfigurationOutput(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectOutput
    CsrExtensions: Optional[CsrExtensionsOutput] = None


class CsrExtensions(BaseValidatorModel):
    KeyUsage: Optional[KeyUsage] = None
    SubjectInformationAccess: Optional[Sequence[AccessDescription]] = None


class GeneralNameUnion(BaseValidatorModel):
    pass


class Extensions(BaseValidatorModel):
    CertificatePolicies: Optional[Sequence[PolicyInformation]] = None
    ExtendedKeyUsage: Optional[Sequence[ExtendedKeyUsage]] = None
    KeyUsage: Optional[KeyUsage] = None
    SubjectAlternativeNames: Optional[Sequence[GeneralNameUnion]] = None
    CustomExtensions: Optional[Sequence[CustomExtension]] = None


class CertificateAuthorityConfiguration(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1Subject
    CsrExtensions: Optional[CsrExtensions] = None


class ApiPassthrough(BaseValidatorModel):
    Extensions: Optional[Extensions] = None
    Subject: Optional[ASN1SubjectUnion] = None


class CertificateAuthority(BaseValidatorModel):
    pass


class DescribeCertificateAuthorityResponse(BaseValidatorModel):
    CertificateAuthority: CertificateAuthority
    ResponseMetadata: ResponseMetadata


class ListCertificateAuthoritiesResponse(BaseValidatorModel):
    CertificateAuthorities: List[CertificateAuthority]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Validity(BaseValidatorModel):
    pass


class IssueCertificateRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Csr: Blob
    SigningAlgorithm: SigningAlgorithmType
    Validity: Validity
    ApiPassthrough: Optional[ApiPassthrough] = None
    TemplateArn: Optional[str] = None
    ValidityNotBefore: Optional[Validity] = None
    IdempotencyToken: Optional[str] = None


class CertificateAuthorityConfigurationUnion(BaseValidatorModel):
    pass


class CreateCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityConfiguration: CertificateAuthorityConfigurationUnion
    CertificateAuthorityType: CertificateAuthorityTypeType
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    IdempotencyToken: Optional[str] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    Tags: Optional[Sequence[Tag]] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None


