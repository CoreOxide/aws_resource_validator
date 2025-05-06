from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.acm_pca.acm_pca_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CustomAttribute(BaseValidatorModel):
    ObjectIdentifier: str
    Value: str


class AccessMethod(BaseValidatorModel):
    CustomObjectIdentifier: Optional[str] = None
    AccessMethodType: Optional[AccessMethodTypeType] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


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
    Actions: List[ActionTypeType]
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


class Validity(BaseValidatorModel):
    Value: int
    Type: ValidityPeriodTypeType


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
    CustomAttributes: Optional[List[CustomAttribute]] = None


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
    Tags: List[Tag]


class UntagCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Tags: List[Tag]


class CrlConfiguration(BaseValidatorModel):
    Enabled: bool
    ExpirationInDays: Optional[int] = None
    CustomCname: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3ObjectAcl: Optional[S3ObjectAclType] = None
    CrlDistributionPointExtensionConfiguration: Optional[CrlDistributionPointExtensionConfiguration] = None
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
    PolicyQualifierId: Literal['CPS']
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

ASN1SubjectUnion = Union[ASN1Subject, ASN1SubjectOutput]


class RevocationConfiguration(BaseValidatorModel):
    CrlConfiguration: Optional[CrlConfiguration] = None
    OcspConfiguration: Optional[OcspConfiguration] = None


class PolicyInformation(BaseValidatorModel):
    CertPolicyId: str
    PolicyQualifiers: Optional[List[PolicyQualifierInfo]] = None


class AccessDescriptionOutput(BaseValidatorModel):
    AccessMethod: AccessMethod
    AccessLocation: GeneralNameOutput


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

GeneralNameUnion = Union[GeneralName, GeneralNameOutput]


class CertificateAuthorityConfigurationOutput(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1SubjectOutput
    CsrExtensions: Optional[CsrExtensionsOutput] = None


class CsrExtensions(BaseValidatorModel):
    KeyUsage: Optional[KeyUsage] = None
    SubjectInformationAccess: Optional[List[AccessDescription]] = None


class Extensions(BaseValidatorModel):
    CertificatePolicies: Optional[List[PolicyInformation]] = None
    ExtendedKeyUsage: Optional[List[ExtendedKeyUsage]] = None
    KeyUsage: Optional[KeyUsage] = None
    SubjectAlternativeNames: Optional[List[GeneralNameUnion]] = None
    CustomExtensions: Optional[List[CustomExtension]] = None


class CertificateAuthority(BaseValidatorModel):
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
    CertificateAuthorityConfiguration: Optional[CertificateAuthorityConfigurationOutput] = None
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    RestorableUntil: Optional[datetime] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None


class CertificateAuthorityConfiguration(BaseValidatorModel):
    KeyAlgorithm: KeyAlgorithmType
    SigningAlgorithm: SigningAlgorithmType
    Subject: ASN1Subject
    CsrExtensions: Optional[CsrExtensions] = None


class ApiPassthrough(BaseValidatorModel):
    Extensions: Optional[Extensions] = None
    Subject: Optional[ASN1SubjectUnion] = None


class DescribeCertificateAuthorityResponse(BaseValidatorModel):
    CertificateAuthority: CertificateAuthority
    ResponseMetadata: ResponseMetadata


class ListCertificateAuthoritiesResponse(BaseValidatorModel):
    CertificateAuthorities: List[CertificateAuthority]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

CertificateAuthorityConfigurationUnion = Union[CertificateAuthorityConfiguration, CertificateAuthorityConfigurationOutput]


class IssueCertificateRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    Csr: Blob
    SigningAlgorithm: SigningAlgorithmType
    Validity: Validity
    ApiPassthrough: Optional[ApiPassthrough] = None
    TemplateArn: Optional[str] = None
    ValidityNotBefore: Optional[Validity] = None
    IdempotencyToken: Optional[str] = None


class CreateCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityConfiguration: CertificateAuthorityConfigurationUnion
    CertificateAuthorityType: CertificateAuthorityTypeType
    RevocationConfiguration: Optional[RevocationConfiguration] = None
    IdempotencyToken: Optional[str] = None
    KeyStorageSecurityStandard: Optional[KeyStorageSecurityStandardType] = None
    Tags: Optional[List[Tag]] = None
    UsageMode: Optional[CertificateAuthorityUsageModeType] = None