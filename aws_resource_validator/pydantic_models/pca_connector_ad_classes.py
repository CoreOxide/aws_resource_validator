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

class VpcInformationPaginatorTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]

class VpcInformationTypeDef(BaseValidatorModel):
    SecurityGroupIds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateDirectoryRegistrationRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateServicePrincipalNameRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str
    ClientToken: Optional[str] = None

class DeleteConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str

class DeleteDirectoryRegistrationRequestRequestTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str

class DeleteServicePrincipalNameRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str

class DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str

class DeleteTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class GetConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str

class GetDirectoryRegistrationRequestRequestTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str

class GetServicePrincipalNameRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str

class ServicePrincipalNameTypeDef(BaseValidatorModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None

class GetTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str

class GetTemplateRequestRequestTypeDef(BaseValidatorModel):
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

class ListConnectorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDirectoryRegistrationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServicePrincipalNamesRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListTemplateGroupAccessControlEntriesRequestRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrivateKeyAttributesV2PaginatorTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class TemplateRevisionTypeDef(BaseValidatorModel):
    MajorRevision: int
    MinorRevision: int

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

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

class CreateTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseValidatorModel):
    AccessRights: AccessRightsTypeDef
    GroupDisplayName: str
    GroupSecurityIdentifier: str
    TemplateArn: str
    ClientToken: Optional[str] = None

class UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str
    AccessRights: Optional[AccessRightsTypeDef] = None
    GroupDisplayName: Optional[str] = None

class ApplicationPoliciesPaginatorTypeDef(BaseValidatorModel):
    Policies: List[ApplicationPolicyTypeDef]
    Critical: Optional[bool] = None

class ApplicationPoliciesTypeDef(BaseValidatorModel):
    Policies: Sequence[ApplicationPolicyTypeDef]
    Critical: Optional[bool] = None

class CertificateValidityTypeDef(BaseValidatorModel):
    RenewalPeriod: ValidityPeriodTypeDef
    ValidityPeriod: ValidityPeriodTypeDef

class ConnectorSummaryPaginatorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationPaginatorTypeDef] = None

class ConnectorSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationTypeDef] = None

class ConnectorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationTypeDef] = None

class CreateConnectorRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: str
    DirectoryId: str
    VpcInformation: VpcInformationTypeDef
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDirectoryRegistrationsRequestListDirectoryRegistrationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePrincipalNamesRequestListServicePrincipalNamesPaginateTypeDef(BaseValidatorModel):
    DirectoryRegistrationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateGroupAccessControlEntriesRequestListTemplateGroupAccessControlEntriesPaginateTypeDef(BaseValidatorModel):
    TemplateArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesRequestListTemplatesPaginateTypeDef(BaseValidatorModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePrincipalNamesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ServicePrincipalNames: List[ServicePrincipalNameSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateGroupAccessControlEntriesResponseTypeDef(BaseValidatorModel):
    AccessControlEntries: List[AccessControlEntrySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateGroupAccessControlEntryResponseTypeDef(BaseValidatorModel):
    AccessControlEntry: AccessControlEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponsePaginatorTypeDef(BaseValidatorModel):
    Connectors: List[ConnectorSummaryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponseTypeDef(BaseValidatorModel):
    Connectors: List[ConnectorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorResponseTypeDef(BaseValidatorModel):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionsV2PaginatorTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesPaginatorTypeDef] = None

class ExtensionsV2TypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None

class ExtensionsV3PaginatorTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesPaginatorTypeDef] = None

class ExtensionsV3TypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None

class ExtensionsV4PaginatorTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesPaginatorTypeDef] = None

class ExtensionsV4TypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None

class PrivateKeyAttributesV3PaginatorTypeDef(BaseValidatorModel):
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

class PrivateKeyAttributesV4PaginatorTypeDef(BaseValidatorModel):
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

class TemplateV2PaginatorTypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV2TypeDef
    Extensions: ExtensionsV2PaginatorTypeDef
    GeneralFlags: GeneralFlagsV2TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV2PaginatorTypeDef
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

class TemplateV3PaginatorTypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV3TypeDef
    Extensions: ExtensionsV3PaginatorTypeDef
    GeneralFlags: GeneralFlagsV3TypeDef
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3PaginatorTypeDef
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

class TemplateV4PaginatorTypeDef(BaseValidatorModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV4TypeDef
    Extensions: ExtensionsV4PaginatorTypeDef
    GeneralFlags: GeneralFlagsV4TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV4PaginatorTypeDef
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

class TemplateDefinitionPaginatorTypeDef(BaseValidatorModel):
    TemplateV2: Optional[TemplateV2PaginatorTypeDef] = None
    TemplateV3: Optional[TemplateV3PaginatorTypeDef] = None
    TemplateV4: Optional[TemplateV4PaginatorTypeDef] = None

class TemplateDefinitionTypeDef(BaseValidatorModel):
    TemplateV2: Optional[TemplateV2TypeDef] = None
    TemplateV3: Optional[TemplateV3TypeDef] = None
    TemplateV4: Optional[TemplateV4TypeDef] = None

class TemplateSummaryPaginatorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Definition: Optional[TemplateDefinitionPaginatorTypeDef] = None
    Name: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicySchema: Optional[int] = None
    Revision: Optional[TemplateRevisionTypeDef] = None
    Status: Optional[TemplateStatusType] = None
    UpdatedAt: Optional[datetime] = None

class CreateTemplateRequestRequestTypeDef(BaseValidatorModel):
    ConnectorArn: str
    Definition: TemplateDefinitionTypeDef
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class TemplateSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Definition: Optional[TemplateDefinitionTypeDef] = None
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
    Definition: Optional[TemplateDefinitionTypeDef] = None
    Name: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicySchema: Optional[int] = None
    Revision: Optional[TemplateRevisionTypeDef] = None
    Status: Optional[TemplateStatusType] = None
    UpdatedAt: Optional[datetime] = None

class UpdateTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateArn: str
    Definition: Optional[TemplateDefinitionTypeDef] = None
    ReenrollAllCertificateHolders: Optional[bool] = None

class ListTemplatesResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    Templates: List[TemplateSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplatesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateResponseTypeDef(BaseValidatorModel):
    Template: TemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

