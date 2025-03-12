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
from aws_resource_validator.pydantic_models.pca_connector_ad_constants import *

class AccessRightsTypeDef(BaseValidatorModel):
    AutoEnroll: Optional[AccessRightType] = None
    Enroll: Optional[AccessRightType] = None


class ApplicationPolicyTypeDef(BaseValidatorModel):
    PolicyObjectIdentifier: Optional[str] = None
    PolicyType: Optional[ApplicationPolicyTypeType] = None


class ValidityPeriodTypeDef(BaseValidatorModel):
    Period: int
    PeriodType: ValidityPeriodTypeType


class VpcInformationOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    IpAddressType: Optional[IpAddressTypeType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDirectoryRegistrationRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateServicePrincipalNameRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str
    ClientToken: Optional[str] = None


class DeleteConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str


class DeleteDirectoryRegistrationRequestTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str


class DeleteServicePrincipalNameRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str


class DeleteTemplateGroupAccessControlEntryRequestTypeDef(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str


class DeleteTemplateRequestTypeDef(BaseValidatorModel):
    TemplateArn: str


class DirectoryRegistrationSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[DirectoryRegistrationStatusType] = None
    StatusReason: Optional[DirectoryRegistrationStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


class DirectoryRegistrationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[DirectoryRegistrationStatusType] = None
    StatusReason: Optional[DirectoryRegistrationStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


class EnrollmentFlagsV2TypeDef(BaseValidatorModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None


class EnrollmentFlagsV3TypeDef(BaseValidatorModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None


class EnrollmentFlagsV4TypeDef(BaseValidatorModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None


class GeneralFlagsV2TypeDef(BaseValidatorModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None


class GeneralFlagsV3TypeDef(BaseValidatorModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None


class GeneralFlagsV4TypeDef(BaseValidatorModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None


class GetConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str


class GetDirectoryRegistrationRequestTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str


class GetServicePrincipalNameRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str


class ServicePrincipalNameTypeDef(BaseValidatorModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


class GetTemplateGroupAccessControlEntryRequestTypeDef(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str


class GetTemplateRequestTypeDef(BaseValidatorModel):
    TemplateArn: str


class KeyUsageFlagsTypeDef(BaseValidatorModel):
    DataEncipherment: Optional[bool] = None
    DigitalSignature: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    KeyEncipherment: Optional[bool] = None
    NonRepudiation: Optional[bool] = None


class KeyUsagePropertyFlagsTypeDef(BaseValidatorModel):
    Decrypt: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    Sign: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListConnectorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDirectoryRegistrationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServicePrincipalNamesRequestTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ServicePrincipalNameSummaryTypeDef(BaseValidatorModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListTemplateGroupAccessControlEntriesRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTemplatesRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PrivateKeyAttributesV2OutputTypeDef(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None


class PrivateKeyAttributesV2TypeDef(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    CryptoProviders: Optional[Sequence[str]] = None


class PrivateKeyFlagsV2TypeDef(BaseValidatorModel):
    ClientVersion: ClientCompatibilityV2Type
    ExportableKey: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None


class PrivateKeyFlagsV3TypeDef(BaseValidatorModel):
    ClientVersion: ClientCompatibilityV3Type
    ExportableKey: Optional[bool] = None
    RequireAlternateSignatureAlgorithm: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None


class PrivateKeyFlagsV4TypeDef(BaseValidatorModel):
    ClientVersion: ClientCompatibilityV4Type
    ExportableKey: Optional[bool] = None
    RequireAlternateSignatureAlgorithm: Optional[bool] = None
    RequireSameKeyRenewal: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None
    UseLegacyProvider: Optional[bool] = None


class SubjectNameFlagsV2TypeDef(BaseValidatorModel):
    RequireCommonName: Optional[bool] = None
    RequireDirectoryPath: Optional[bool] = None
    RequireDnsAsCn: Optional[bool] = None
    RequireEmail: Optional[bool] = None
    SanRequireDirectoryGuid: Optional[bool] = None
    SanRequireDns: Optional[bool] = None
    SanRequireDomainDns: Optional[bool] = None
    SanRequireEmail: Optional[bool] = None
    SanRequireSpn: Optional[bool] = None
    SanRequireUpn: Optional[bool] = None


class SubjectNameFlagsV3TypeDef(BaseValidatorModel):
    RequireCommonName: Optional[bool] = None
    RequireDirectoryPath: Optional[bool] = None
    RequireDnsAsCn: Optional[bool] = None
    RequireEmail: Optional[bool] = None
    SanRequireDirectoryGuid: Optional[bool] = None
    SanRequireDns: Optional[bool] = None
    SanRequireDomainDns: Optional[bool] = None
    SanRequireEmail: Optional[bool] = None
    SanRequireSpn: Optional[bool] = None
    SanRequireUpn: Optional[bool] = None


class SubjectNameFlagsV4TypeDef(BaseValidatorModel):
    RequireCommonName: Optional[bool] = None
    RequireDirectoryPath: Optional[bool] = None
    RequireDnsAsCn: Optional[bool] = None
    RequireEmail: Optional[bool] = None
    SanRequireDirectoryGuid: Optional[bool] = None
    SanRequireDns: Optional[bool] = None
    SanRequireDomainDns: Optional[bool] = None
    SanRequireEmail: Optional[bool] = None
    SanRequireSpn: Optional[bool] = None
    SanRequireUpn: Optional[bool] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class TemplateRevisionTypeDef(BaseValidatorModel):
    MajorRevision: int
    MinorRevision: int


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class VpcInformationTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]
    IpAddressType: Optional[IpAddressTypeType] = None


class AccessControlEntrySummaryTypeDef(BaseValidatorModel):
    AccessRights: Optional[AccessRightsTypeDef] = None
    CreatedAt: Optional[datetime] = None
    GroupDisplayName: Optional[str] = None
    GroupSecurityIdentifier: Optional[str] = None
    TemplateArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class AccessControlEntryTypeDef(BaseValidatorModel):
    AccessRights: Optional[AccessRightsTypeDef] = None
    CreatedAt: Optional[datetime] = None
    GroupDisplayName: Optional[str] = None
    GroupSecurityIdentifier: Optional[str] = None
    TemplateArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class CreateTemplateGroupAccessControlEntryRequestTypeDef(BaseValidatorModel):
    AccessRights: AccessRightsTypeDef
    GroupDisplayName: str
    GroupSecurityIdentifier: str
    TemplateArn: str
    ClientToken: Optional[str] = None


class UpdateTemplateGroupAccessControlEntryRequestTypeDef(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str
    AccessRights: Optional[AccessRightsTypeDef] = None
    GroupDisplayName: Optional[str] = None


class ApplicationPoliciesOutputTypeDef(BaseValidatorModel):
    Policies: List[ApplicationPolicyTypeDef]
    Critical: Optional[bool] = None


class ApplicationPoliciesTypeDef(BaseValidatorModel):
    Policies: Sequence[ApplicationPolicyTypeDef]
    Critical: Optional[bool] = None


class CertificateValidityTypeDef(BaseValidatorModel):
    RenewalPeriod: ValidityPeriodTypeDef
    ValidityPeriod: ValidityPeriodTypeDef


class ConnectorSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationOutputTypeDef] = None


class ConnectorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationOutputTypeDef] = None


class CreateConnectorResponseTypeDef(BaseValidatorModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDirectoryRegistrationResponseTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTemplateResponseTypeDef(BaseValidatorModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDirectoryRegistrationsResponseTypeDef(BaseValidatorModel):
    DirectoryRegistrations: List[DirectoryRegistrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDirectoryRegistrationResponseTypeDef(BaseValidatorModel):
    DirectoryRegistration: DirectoryRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetServicePrincipalNameResponseTypeDef(BaseValidatorModel):
    ServicePrincipalName: ServicePrincipalNameTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class KeyUsageTypeDef(BaseValidatorModel):
    UsageFlags: KeyUsageFlagsTypeDef
    Critical: Optional[bool] = None


class KeyUsagePropertyTypeDef(BaseValidatorModel):
    PropertyFlags: Optional[KeyUsagePropertyFlagsTypeDef] = None
    PropertyType: Optional[Literal["ALL"]] = None


class ListConnectorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDirectoryRegistrationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicePrincipalNamesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTemplateGroupAccessControlEntriesRequestPaginateTypeDef(BaseValidatorModel):
    TemplateArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicePrincipalNamesResponseTypeDef(BaseValidatorModel):
    ServicePrincipalNames: List[ServicePrincipalNameSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTemplateGroupAccessControlEntriesResponseTypeDef(BaseValidatorModel):
    AccessControlEntries: List[AccessControlEntrySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTemplateGroupAccessControlEntryResponseTypeDef(BaseValidatorModel):
    AccessControlEntry: AccessControlEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListConnectorsResponseTypeDef(BaseValidatorModel):
    Connectors: List[ConnectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetConnectorResponseTypeDef(BaseValidatorModel):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExtensionsV2OutputTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesOutputTypeDef] = None


class ExtensionsV2TypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None


class ExtensionsV3OutputTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesOutputTypeDef] = None


class ExtensionsV3TypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None


class ExtensionsV4OutputTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesOutputTypeDef] = None


class ExtensionsV4TypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None


class PrivateKeyAttributesV3OutputTypeDef(BaseValidatorModel):
    Algorithm: PrivateKeyAlgorithmType
    KeySpec: KeySpecType
    KeyUsageProperty: KeyUsagePropertyTypeDef
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None


class PrivateKeyAttributesV3TypeDef(BaseValidatorModel):
    Algorithm: PrivateKeyAlgorithmType
    KeySpec: KeySpecType
    KeyUsageProperty: KeyUsagePropertyTypeDef
    MinimalKeyLength: int
    CryptoProviders: Optional[Sequence[str]] = None


class PrivateKeyAttributesV4OutputTypeDef(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    Algorithm: Optional[PrivateKeyAlgorithmType] = None
    CryptoProviders: Optional[List[str]] = None
    KeyUsageProperty: Optional[KeyUsagePropertyTypeDef] = None


class PrivateKeyAttributesV4TypeDef(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    Algorithm: Optional[PrivateKeyAlgorithmType] = None
    CryptoProviders: Optional[Sequence[str]] = None
    KeyUsageProperty: Optional[KeyUsagePropertyTypeDef] = None


class VpcInformationUnionTypeDef(BaseValidatorModel):
    pass


class CreateConnectorRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    DirectoryId: str
    VpcInformation: VpcInformationUnionTypeDef
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class TemplateV2OutputTypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV2TypeDef
    Extensions: ExtensionsV2OutputTypeDef
    GeneralFlags: GeneralFlagsV2TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV2OutputTypeDef
    PrivateKeyFlags: PrivateKeyFlagsV2TypeDef
    SubjectNameFlags: SubjectNameFlagsV2TypeDef
    SupersededTemplates: Optional[List[str]] = None


class TemplateV2TypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV2TypeDef
    Extensions: ExtensionsV2TypeDef
    GeneralFlags: GeneralFlagsV2TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV2TypeDef
    PrivateKeyFlags: PrivateKeyFlagsV2TypeDef
    SubjectNameFlags: SubjectNameFlagsV2TypeDef
    SupersededTemplates: Optional[Sequence[str]] = None


class TemplateV3OutputTypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV3TypeDef
    Extensions: ExtensionsV3OutputTypeDef
    GeneralFlags: GeneralFlagsV3TypeDef
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3OutputTypeDef
    PrivateKeyFlags: PrivateKeyFlagsV3TypeDef
    SubjectNameFlags: SubjectNameFlagsV3TypeDef
    SupersededTemplates: Optional[List[str]] = None


class TemplateV3TypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV3TypeDef
    Extensions: ExtensionsV3TypeDef
    GeneralFlags: GeneralFlagsV3TypeDef
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3TypeDef
    PrivateKeyFlags: PrivateKeyFlagsV3TypeDef
    SubjectNameFlags: SubjectNameFlagsV3TypeDef
    SupersededTemplates: Optional[Sequence[str]] = None


class TemplateV4OutputTypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV4TypeDef
    Extensions: ExtensionsV4OutputTypeDef
    GeneralFlags: GeneralFlagsV4TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV4OutputTypeDef
    PrivateKeyFlags: PrivateKeyFlagsV4TypeDef
    SubjectNameFlags: SubjectNameFlagsV4TypeDef
    HashAlgorithm: Optional[HashAlgorithmType] = None
    SupersededTemplates: Optional[List[str]] = None


class TemplateV4TypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV4TypeDef
    Extensions: ExtensionsV4TypeDef
    GeneralFlags: GeneralFlagsV4TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV4TypeDef
    PrivateKeyFlags: PrivateKeyFlagsV4TypeDef
    SubjectNameFlags: SubjectNameFlagsV4TypeDef
    HashAlgorithm: Optional[HashAlgorithmType] = None
    SupersededTemplates: Optional[Sequence[str]] = None


class TemplateDefinitionOutputTypeDef(BaseValidatorModel):
    TemplateV2: Optional[TemplateV2OutputTypeDef] = None
    TemplateV3: Optional[TemplateV3OutputTypeDef] = None
    TemplateV4: Optional[TemplateV4OutputTypeDef] = None


class TemplateDefinitionTypeDef(BaseValidatorModel):
    TemplateV2: Optional[TemplateV2TypeDef] = None
    TemplateV3: Optional[TemplateV3TypeDef] = None
    TemplateV4: Optional[TemplateV4TypeDef] = None


class TemplateSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Definition: Optional[TemplateDefinitionOutputTypeDef] = None
    Name: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicySchema: Optional[int] = None
    Revision: Optional[TemplateRevisionTypeDef] = None
    Status: Optional[TemplateStatusType] = None
    UpdatedAt: Optional[datetime] = None


class TemplateTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Definition: Optional[TemplateDefinitionOutputTypeDef] = None
    Name: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicySchema: Optional[int] = None
    Revision: Optional[TemplateRevisionTypeDef] = None
    Status: Optional[TemplateStatusType] = None
    UpdatedAt: Optional[datetime] = None


class ListTemplatesResponseTypeDef(BaseValidatorModel):
    Templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTemplateResponseTypeDef(BaseValidatorModel):
    Template: TemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TemplateDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class CreateTemplateRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    Definition: TemplateDefinitionUnionTypeDef
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateTemplateRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    Definition: Optional[TemplateDefinitionUnionTypeDef] = None
    ReenrollAllCertificateHolders: Optional[bool] = None


