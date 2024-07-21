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
from aws_resource_validator.pydantic_models.pca_connector_ad_constants import *

class AccessRightsTypeDef(BaseModel):
    AutoEnroll: Optional[AccessRightType] = None
    Enroll: Optional[AccessRightType] = None

class ApplicationPolicyTypeDef(BaseModel):
    PolicyObjectIdentifier: Optional[str] = None
    PolicyType: Optional[ApplicationPolicyTypeType] = None

class ValidityPeriodTypeDef(BaseModel):
    Period: int
    PeriodType: ValidityPeriodTypeType

class VpcInformationPaginatorTypeDef(BaseModel):
    SecurityGroupIds: List[str]

class VpcInformationTypeDef(BaseModel):
    SecurityGroupIds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateDirectoryRegistrationRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateServicePrincipalNameRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str
    ClientToken: Optional[str] = None

class DeleteConnectorRequestRequestTypeDef(BaseModel):
    ConnectorArn: str

class DeleteDirectoryRegistrationRequestRequestTypeDef(BaseModel):
    DirectoryRegistrationArn: str

class DeleteServicePrincipalNameRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str

class DeleteTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseModel):
    GroupSecurityIdentifier: str
    TemplateArn: str

class DeleteTemplateRequestRequestTypeDef(BaseModel):
    TemplateArn: str

class DirectoryRegistrationSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[DirectoryRegistrationStatusType] = None
    StatusReason: Optional[DirectoryRegistrationStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None

class DirectoryRegistrationTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[DirectoryRegistrationStatusType] = None
    StatusReason: Optional[DirectoryRegistrationStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None

class EnrollmentFlagsV2TypeDef(BaseModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None

class EnrollmentFlagsV3TypeDef(BaseModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None

class EnrollmentFlagsV4TypeDef(BaseModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None

class GeneralFlagsV2TypeDef(BaseModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None

class GeneralFlagsV3TypeDef(BaseModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None

class GeneralFlagsV4TypeDef(BaseModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None

class GetConnectorRequestRequestTypeDef(BaseModel):
    ConnectorArn: str

class GetDirectoryRegistrationRequestRequestTypeDef(BaseModel):
    DirectoryRegistrationArn: str

class GetServicePrincipalNameRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str

class ServicePrincipalNameTypeDef(BaseModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None

class GetTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseModel):
    GroupSecurityIdentifier: str
    TemplateArn: str

class GetTemplateRequestRequestTypeDef(BaseModel):
    TemplateArn: str

class KeyUsageFlagsTypeDef(BaseModel):
    DataEncipherment: Optional[bool] = None
    DigitalSignature: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    KeyEncipherment: Optional[bool] = None
    NonRepudiation: Optional[bool] = None

class KeyUsagePropertyFlagsTypeDef(BaseModel):
    Decrypt: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    Sign: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDirectoryRegistrationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServicePrincipalNamesRequestRequestTypeDef(BaseModel):
    DirectoryRegistrationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ServicePrincipalNameSummaryTypeDef(BaseModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListTemplateGroupAccessControlEntriesRequestRequestTypeDef(BaseModel):
    TemplateArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTemplatesRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrivateKeyAttributesV2PaginatorTypeDef(BaseModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None

class PrivateKeyAttributesV2TypeDef(BaseModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    CryptoProviders: Optional[Sequence[str]] = None

class PrivateKeyFlagsV2TypeDef(BaseModel):
    ClientVersion: ClientCompatibilityV2Type
    ExportableKey: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None

class PrivateKeyFlagsV3TypeDef(BaseModel):
    ClientVersion: ClientCompatibilityV3Type
    ExportableKey: Optional[bool] = None
    RequireAlternateSignatureAlgorithm: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None

class PrivateKeyFlagsV4TypeDef(BaseModel):
    ClientVersion: ClientCompatibilityV4Type
    ExportableKey: Optional[bool] = None
    RequireAlternateSignatureAlgorithm: Optional[bool] = None
    RequireSameKeyRenewal: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None
    UseLegacyProvider: Optional[bool] = None

class SubjectNameFlagsV2TypeDef(BaseModel):
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

class SubjectNameFlagsV3TypeDef(BaseModel):
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

class SubjectNameFlagsV4TypeDef(BaseModel):
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

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class TemplateRevisionTypeDef(BaseModel):
    MajorRevision: int
    MinorRevision: int

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AccessControlEntrySummaryTypeDef(BaseModel):
    AccessRights: Optional[AccessRightsTypeDef] = None
    CreatedAt: Optional[datetime] = None
    GroupDisplayName: Optional[str] = None
    GroupSecurityIdentifier: Optional[str] = None
    TemplateArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None

class AccessControlEntryTypeDef(BaseModel):
    AccessRights: Optional[AccessRightsTypeDef] = None
    CreatedAt: Optional[datetime] = None
    GroupDisplayName: Optional[str] = None
    GroupSecurityIdentifier: Optional[str] = None
    TemplateArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None

class CreateTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseModel):
    AccessRights: AccessRightsTypeDef
    GroupDisplayName: str
    GroupSecurityIdentifier: str
    TemplateArn: str
    ClientToken: Optional[str] = None

class UpdateTemplateGroupAccessControlEntryRequestRequestTypeDef(BaseModel):
    GroupSecurityIdentifier: str
    TemplateArn: str
    AccessRights: Optional[AccessRightsTypeDef] = None
    GroupDisplayName: Optional[str] = None

class ApplicationPoliciesPaginatorTypeDef(BaseModel):
    Policies: List[ApplicationPolicyTypeDef]
    Critical: Optional[bool] = None

class ApplicationPoliciesTypeDef(BaseModel):
    Policies: Sequence[ApplicationPolicyTypeDef]
    Critical: Optional[bool] = None

class CertificateValidityTypeDef(BaseModel):
    RenewalPeriod: ValidityPeriodTypeDef
    ValidityPeriod: ValidityPeriodTypeDef

class ConnectorSummaryPaginatorTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationPaginatorTypeDef] = None

class ConnectorSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationTypeDef] = None

class ConnectorTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationTypeDef] = None

class CreateConnectorRequestRequestTypeDef(BaseModel):
    CertificateAuthorityArn: str
    DirectoryId: str
    VpcInformation: VpcInformationTypeDef
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateConnectorResponseTypeDef(BaseModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryRegistrationResponseTypeDef(BaseModel):
    DirectoryRegistrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(BaseModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDirectoryRegistrationsResponseTypeDef(BaseModel):
    DirectoryRegistrations: List[DirectoryRegistrationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDirectoryRegistrationResponseTypeDef(BaseModel):
    DirectoryRegistration: DirectoryRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServicePrincipalNameResponseTypeDef(BaseModel):
    ServicePrincipalName: ServicePrincipalNameTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KeyUsageTypeDef(BaseModel):
    UsageFlags: KeyUsageFlagsTypeDef
    Critical: Optional[bool] = None

class KeyUsagePropertyTypeDef(BaseModel):
    PropertyFlags: Optional[KeyUsagePropertyFlagsTypeDef] = None
    PropertyType: Optional[Literal["ALL"]] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDirectoryRegistrationsRequestListDirectoryRegistrationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePrincipalNamesRequestListServicePrincipalNamesPaginateTypeDef(BaseModel):
    DirectoryRegistrationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplateGroupAccessControlEntriesRequestListTemplateGroupAccessControlEntriesPaginateTypeDef(BaseModel):
    TemplateArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTemplatesRequestListTemplatesPaginateTypeDef(BaseModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicePrincipalNamesResponseTypeDef(BaseModel):
    NextToken: str
    ServicePrincipalNames: List[ServicePrincipalNameSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplateGroupAccessControlEntriesResponseTypeDef(BaseModel):
    AccessControlEntries: List[AccessControlEntrySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateGroupAccessControlEntryResponseTypeDef(BaseModel):
    AccessControlEntry: AccessControlEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponsePaginatorTypeDef(BaseModel):
    Connectors: List[ConnectorSummaryPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorsResponseTypeDef(BaseModel):
    Connectors: List[ConnectorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorResponseTypeDef(BaseModel):
    Connector: ConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionsV2PaginatorTypeDef(BaseModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesPaginatorTypeDef] = None

class ExtensionsV2TypeDef(BaseModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None

class ExtensionsV3PaginatorTypeDef(BaseModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesPaginatorTypeDef] = None

class ExtensionsV3TypeDef(BaseModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None

class ExtensionsV4PaginatorTypeDef(BaseModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesPaginatorTypeDef] = None

class ExtensionsV4TypeDef(BaseModel):
    KeyUsage: KeyUsageTypeDef
    ApplicationPolicies: Optional[ApplicationPoliciesTypeDef] = None

class PrivateKeyAttributesV3PaginatorTypeDef(BaseModel):
    Algorithm: PrivateKeyAlgorithmType
    KeySpec: KeySpecType
    KeyUsageProperty: KeyUsagePropertyTypeDef
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None

class PrivateKeyAttributesV3TypeDef(BaseModel):
    Algorithm: PrivateKeyAlgorithmType
    KeySpec: KeySpecType
    KeyUsageProperty: KeyUsagePropertyTypeDef
    MinimalKeyLength: int
    CryptoProviders: Optional[Sequence[str]] = None

class PrivateKeyAttributesV4PaginatorTypeDef(BaseModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    Algorithm: Optional[PrivateKeyAlgorithmType] = None
    CryptoProviders: Optional[List[str]] = None
    KeyUsageProperty: Optional[KeyUsagePropertyTypeDef] = None

class PrivateKeyAttributesV4TypeDef(BaseModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    Algorithm: Optional[PrivateKeyAlgorithmType] = None
    CryptoProviders: Optional[Sequence[str]] = None
    KeyUsageProperty: Optional[KeyUsagePropertyTypeDef] = None

class TemplateV2PaginatorTypeDef(BaseModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV2TypeDef
    Extensions: ExtensionsV2PaginatorTypeDef
    GeneralFlags: GeneralFlagsV2TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV2PaginatorTypeDef
    PrivateKeyFlags: PrivateKeyFlagsV2TypeDef
    SubjectNameFlags: SubjectNameFlagsV2TypeDef
    SupersededTemplates: Optional[List[str]] = None

class TemplateV2TypeDef(BaseModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV2TypeDef
    Extensions: ExtensionsV2TypeDef
    GeneralFlags: GeneralFlagsV2TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV2TypeDef
    PrivateKeyFlags: PrivateKeyFlagsV2TypeDef
    SubjectNameFlags: SubjectNameFlagsV2TypeDef
    SupersededTemplates: Optional[Sequence[str]] = None

class TemplateV3PaginatorTypeDef(BaseModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV3TypeDef
    Extensions: ExtensionsV3PaginatorTypeDef
    GeneralFlags: GeneralFlagsV3TypeDef
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3PaginatorTypeDef
    PrivateKeyFlags: PrivateKeyFlagsV3TypeDef
    SubjectNameFlags: SubjectNameFlagsV3TypeDef
    SupersededTemplates: Optional[List[str]] = None

class TemplateV3TypeDef(BaseModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV3TypeDef
    Extensions: ExtensionsV3TypeDef
    GeneralFlags: GeneralFlagsV3TypeDef
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3TypeDef
    PrivateKeyFlags: PrivateKeyFlagsV3TypeDef
    SubjectNameFlags: SubjectNameFlagsV3TypeDef
    SupersededTemplates: Optional[Sequence[str]] = None

class TemplateV4PaginatorTypeDef(BaseModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV4TypeDef
    Extensions: ExtensionsV4PaginatorTypeDef
    GeneralFlags: GeneralFlagsV4TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV4PaginatorTypeDef
    PrivateKeyFlags: PrivateKeyFlagsV4TypeDef
    SubjectNameFlags: SubjectNameFlagsV4TypeDef
    HashAlgorithm: Optional[HashAlgorithmType] = None
    SupersededTemplates: Optional[List[str]] = None

class TemplateV4TypeDef(BaseModel):
    CertificateValidity: CertificateValidityTypeDef
    EnrollmentFlags: EnrollmentFlagsV4TypeDef
    Extensions: ExtensionsV4TypeDef
    GeneralFlags: GeneralFlagsV4TypeDef
    PrivateKeyAttributes: PrivateKeyAttributesV4TypeDef
    PrivateKeyFlags: PrivateKeyFlagsV4TypeDef
    SubjectNameFlags: SubjectNameFlagsV4TypeDef
    HashAlgorithm: Optional[HashAlgorithmType] = None
    SupersededTemplates: Optional[Sequence[str]] = None

class TemplateDefinitionPaginatorTypeDef(BaseModel):
    TemplateV2: Optional[TemplateV2PaginatorTypeDef] = None
    TemplateV3: Optional[TemplateV3PaginatorTypeDef] = None
    TemplateV4: Optional[TemplateV4PaginatorTypeDef] = None

class TemplateDefinitionTypeDef(BaseModel):
    TemplateV2: Optional[TemplateV2TypeDef] = None
    TemplateV3: Optional[TemplateV3TypeDef] = None
    TemplateV4: Optional[TemplateV4TypeDef] = None

class TemplateSummaryPaginatorTypeDef(BaseModel):
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

class CreateTemplateRequestRequestTypeDef(BaseModel):
    ConnectorArn: str
    Definition: TemplateDefinitionTypeDef
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class TemplateSummaryTypeDef(BaseModel):
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

class TemplateTypeDef(BaseModel):
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

class UpdateTemplateRequestRequestTypeDef(BaseModel):
    TemplateArn: str
    Definition: Optional[TemplateDefinitionTypeDef] = None
    ReenrollAllCertificateHolders: Optional[bool] = None

class ListTemplatesResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    Templates: List[TemplateSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTemplatesResponseTypeDef(BaseModel):
    NextToken: str
    Templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateResponseTypeDef(BaseModel):
    Template: TemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

