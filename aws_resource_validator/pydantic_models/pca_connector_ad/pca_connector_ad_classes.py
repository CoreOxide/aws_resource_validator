from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pca_connector_ad.pca_connector_ad_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessRights(BaseValidatorModel):
    AutoEnroll: Optional[AccessRightType] = None
    Enroll: Optional[AccessRightType] = None


class ApplicationPolicy(BaseValidatorModel):
    PolicyObjectIdentifier: Optional[str] = None
    PolicyType: Optional[ApplicationPolicyTypeType] = None


class ValidityPeriod(BaseValidatorModel):
    Period: int
    PeriodType: ValidityPeriodTypeType


class VpcInformationOutput(BaseValidatorModel):
    SecurityGroupIds: List[str]
    IpAddressType: Optional[IpAddressTypeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_directory_registration' function.
class CreateDirectoryRegistrationRequest(BaseValidatorModel):
    DirectoryId: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_service_principal_name' function.
class CreateServicePrincipalNameRequest(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_connector' function.
class DeleteConnectorRequest(BaseValidatorModel):
    ConnectorArn: str


# This class is the input for the 'delete_directory_registration' function.
class DeleteDirectoryRegistrationRequest(BaseValidatorModel):
    DirectoryRegistrationArn: str


# This class is the input for the 'delete_service_principal_name' function.
class DeleteServicePrincipalNameRequest(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str


# This class is the input for the 'delete_template_group_access_control_entry' function.
class DeleteTemplateGroupAccessControlEntryRequest(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str


# This class is the input for the 'delete_template' function.
class DeleteTemplateRequest(BaseValidatorModel):
    TemplateArn: str


class DirectoryRegistrationSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[DirectoryRegistrationStatusType] = None
    StatusReason: Optional[DirectoryRegistrationStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


class DirectoryRegistration(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[DirectoryRegistrationStatusType] = None
    StatusReason: Optional[DirectoryRegistrationStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


class EnrollmentFlagsV2(BaseValidatorModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None


class EnrollmentFlagsV3(BaseValidatorModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None


class EnrollmentFlagsV4(BaseValidatorModel):
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool] = None
    IncludeSymmetricAlgorithms: Optional[bool] = None
    NoSecurityExtension: Optional[bool] = None
    RemoveInvalidCertificateFromPersonalStore: Optional[bool] = None
    UserInteractionRequired: Optional[bool] = None


class GeneralFlagsV2(BaseValidatorModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None


class GeneralFlagsV3(BaseValidatorModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None


class GeneralFlagsV4(BaseValidatorModel):
    AutoEnrollment: Optional[bool] = None
    MachineType: Optional[bool] = None


# This class is the input for the 'get_connector' function.
class GetConnectorRequest(BaseValidatorModel):
    ConnectorArn: str


# This class is the input for the 'get_directory_registration' function.
class GetDirectoryRegistrationRequest(BaseValidatorModel):
    DirectoryRegistrationArn: str


# This class is the input for the 'get_service_principal_name' function.
class GetServicePrincipalNameRequest(BaseValidatorModel):
    ConnectorArn: str
    DirectoryRegistrationArn: str


class ServicePrincipalName(BaseValidatorModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'get_template_group_access_control_entry' function.
class GetTemplateGroupAccessControlEntryRequest(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str


# This class is the input for the 'get_template' function.
class GetTemplateRequest(BaseValidatorModel):
    TemplateArn: str


class KeyUsageFlags(BaseValidatorModel):
    DataEncipherment: Optional[bool] = None
    DigitalSignature: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    KeyEncipherment: Optional[bool] = None
    NonRepudiation: Optional[bool] = None


class KeyUsagePropertyFlags(BaseValidatorModel):
    Decrypt: Optional[bool] = None
    KeyAgreement: Optional[bool] = None
    Sign: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_connectors' function.
class ListConnectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_directory_registrations' function.
class ListDirectoryRegistrationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_service_principal_names' function.
class ListServicePrincipalNamesRequest(BaseValidatorModel):
    DirectoryRegistrationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ServicePrincipalNameSummary(BaseValidatorModel):
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryRegistrationArn: Optional[str] = None
    Status: Optional[ServicePrincipalNameStatusType] = None
    StatusReason: Optional[ServicePrincipalNameStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_template_group_access_control_entries' function.
class ListTemplateGroupAccessControlEntriesRequest(BaseValidatorModel):
    TemplateArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_templates' function.
class ListTemplatesRequest(BaseValidatorModel):
    ConnectorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PrivateKeyAttributesV2Output(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None


class PrivateKeyAttributesV2(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None


class PrivateKeyFlagsV2(BaseValidatorModel):
    ClientVersion: ClientCompatibilityV2Type
    ExportableKey: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None


class PrivateKeyFlagsV3(BaseValidatorModel):
    ClientVersion: ClientCompatibilityV3Type
    ExportableKey: Optional[bool] = None
    RequireAlternateSignatureAlgorithm: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None


class PrivateKeyFlagsV4(BaseValidatorModel):
    ClientVersion: ClientCompatibilityV4Type
    ExportableKey: Optional[bool] = None
    RequireAlternateSignatureAlgorithm: Optional[bool] = None
    RequireSameKeyRenewal: Optional[bool] = None
    StrongKeyProtectionRequired: Optional[bool] = None
    UseLegacyProvider: Optional[bool] = None


class SubjectNameFlagsV2(BaseValidatorModel):
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


class SubjectNameFlagsV3(BaseValidatorModel):
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


class SubjectNameFlagsV4(BaseValidatorModel):
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


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class TemplateRevision(BaseValidatorModel):
    MajorRevision: int
    MinorRevision: int


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class VpcInformation(BaseValidatorModel):
    SecurityGroupIds: List[str]
    IpAddressType: Optional[IpAddressTypeType] = None


class AccessControlEntrySummary(BaseValidatorModel):
    AccessRights: Optional[AccessRights] = None
    CreatedAt: Optional[datetime] = None
    GroupDisplayName: Optional[str] = None
    GroupSecurityIdentifier: Optional[str] = None
    TemplateArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class AccessControlEntry(BaseValidatorModel):
    AccessRights: Optional[AccessRights] = None
    CreatedAt: Optional[datetime] = None
    GroupDisplayName: Optional[str] = None
    GroupSecurityIdentifier: Optional[str] = None
    TemplateArn: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'create_template_group_access_control_entry' function.
class CreateTemplateGroupAccessControlEntryRequest(BaseValidatorModel):
    AccessRights: AccessRights
    GroupDisplayName: str
    GroupSecurityIdentifier: str
    TemplateArn: str
    ClientToken: Optional[str] = None


# This class is the input for the 'update_template_group_access_control_entry' function.
class UpdateTemplateGroupAccessControlEntryRequest(BaseValidatorModel):
    GroupSecurityIdentifier: str
    TemplateArn: str
    AccessRights: Optional[AccessRights] = None
    GroupDisplayName: Optional[str] = None


class ApplicationPoliciesOutput(BaseValidatorModel):
    Policies: List[ApplicationPolicy]
    Critical: Optional[bool] = None


class ApplicationPolicies(BaseValidatorModel):
    Policies: List[ApplicationPolicy]
    Critical: Optional[bool] = None


class CertificateValidity(BaseValidatorModel):
    RenewalPeriod: ValidityPeriod
    ValidityPeriod: ValidityPeriod


class ConnectorSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationOutput] = None


class Connector(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityArn: Optional[str] = None
    CertificateEnrollmentPolicyServerEndpoint: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    DirectoryId: Optional[str] = None
    Status: Optional[ConnectorStatusType] = None
    StatusReason: Optional[ConnectorStatusReasonType] = None
    UpdatedAt: Optional[datetime] = None
    VpcInformation: Optional[VpcInformationOutput] = None


# This class is the output for the 'create_connector' function.
class CreateConnectorResponse(BaseValidatorModel):
    ConnectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_directory_registration' function.
class CreateDirectoryRegistrationResponse(BaseValidatorModel):
    DirectoryRegistrationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_template' function.
class CreateTemplateResponse(BaseValidatorModel):
    TemplateArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_template_group_access_control_entry' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_directory_registrations' function.
class ListDirectoryRegistrationsResponse(BaseValidatorModel):
    DirectoryRegistrations: List[DirectoryRegistrationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_directory_registration' function.
class GetDirectoryRegistrationResponse(BaseValidatorModel):
    DirectoryRegistration: DirectoryRegistration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_principal_name' function.
class GetServicePrincipalNameResponse(BaseValidatorModel):
    ServicePrincipalName: ServicePrincipalName
    ResponseMetadata: ResponseMetadata


class KeyUsage(BaseValidatorModel):
    UsageFlags: KeyUsageFlags
    Critical: Optional[bool] = None


class KeyUsageProperty(BaseValidatorModel):
    PropertyFlags: Optional[KeyUsagePropertyFlags] = None
    PropertyType: Optional[Literal['ALL']] = None


class ListConnectorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDirectoryRegistrationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicePrincipalNamesRequestPaginate(BaseValidatorModel):
    DirectoryRegistrationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplateGroupAccessControlEntriesRequestPaginate(BaseValidatorModel):
    TemplateArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTemplatesRequestPaginate(BaseValidatorModel):
    ConnectorArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_service_principal_names' function.
class ListServicePrincipalNamesResponse(BaseValidatorModel):
    ServicePrincipalNames: List[ServicePrincipalNameSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

VpcInformationUnion = Union[VpcInformation, VpcInformationOutput]


# This class is the output for the 'list_template_group_access_control_entries' function.
class ListTemplateGroupAccessControlEntriesResponse(BaseValidatorModel):
    AccessControlEntries: List[AccessControlEntrySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_template_group_access_control_entry' function.
class GetTemplateGroupAccessControlEntryResponse(BaseValidatorModel):
    AccessControlEntry: AccessControlEntry
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_connectors' function.
class ListConnectorsResponse(BaseValidatorModel):
    Connectors: List[ConnectorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_connector' function.
class GetConnectorResponse(BaseValidatorModel):
    Connector: Connector
    ResponseMetadata: ResponseMetadata


class ExtensionsV2Output(BaseValidatorModel):
    KeyUsage: KeyUsage
    ApplicationPolicies: Optional[ApplicationPoliciesOutput] = None


class ExtensionsV2(BaseValidatorModel):
    KeyUsage: KeyUsage
    ApplicationPolicies: Optional[ApplicationPolicies] = None


class ExtensionsV3Output(BaseValidatorModel):
    KeyUsage: KeyUsage
    ApplicationPolicies: Optional[ApplicationPoliciesOutput] = None


class ExtensionsV3(BaseValidatorModel):
    KeyUsage: KeyUsage
    ApplicationPolicies: Optional[ApplicationPolicies] = None


class ExtensionsV4Output(BaseValidatorModel):
    KeyUsage: KeyUsage
    ApplicationPolicies: Optional[ApplicationPoliciesOutput] = None


class ExtensionsV4(BaseValidatorModel):
    KeyUsage: KeyUsage
    ApplicationPolicies: Optional[ApplicationPolicies] = None


class PrivateKeyAttributesV3Output(BaseValidatorModel):
    Algorithm: PrivateKeyAlgorithmType
    KeySpec: KeySpecType
    KeyUsageProperty: KeyUsageProperty
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None


class PrivateKeyAttributesV3(BaseValidatorModel):
    Algorithm: PrivateKeyAlgorithmType
    KeySpec: KeySpecType
    KeyUsageProperty: KeyUsageProperty
    MinimalKeyLength: int
    CryptoProviders: Optional[List[str]] = None


class PrivateKeyAttributesV4Output(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    Algorithm: Optional[PrivateKeyAlgorithmType] = None
    CryptoProviders: Optional[List[str]] = None
    KeyUsageProperty: Optional[KeyUsageProperty] = None


class PrivateKeyAttributesV4(BaseValidatorModel):
    KeySpec: KeySpecType
    MinimalKeyLength: int
    Algorithm: Optional[PrivateKeyAlgorithmType] = None
    CryptoProviders: Optional[List[str]] = None
    KeyUsageProperty: Optional[KeyUsageProperty] = None


# This class is the input for the 'create_connector' function.
class CreateConnectorRequest(BaseValidatorModel):
    CertificateAuthorityArn: str
    DirectoryId: str
    VpcInformation: VpcInformationUnion
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class TemplateV2Output(BaseValidatorModel):
    CertificateValidity: CertificateValidity
    EnrollmentFlags: EnrollmentFlagsV2
    Extensions: ExtensionsV2Output
    GeneralFlags: GeneralFlagsV2
    PrivateKeyAttributes: PrivateKeyAttributesV2Output
    PrivateKeyFlags: PrivateKeyFlagsV2
    SubjectNameFlags: SubjectNameFlagsV2
    SupersededTemplates: Optional[List[str]] = None


class TemplateV2(BaseValidatorModel):
    CertificateValidity: CertificateValidity
    EnrollmentFlags: EnrollmentFlagsV2
    Extensions: ExtensionsV2
    GeneralFlags: GeneralFlagsV2
    PrivateKeyAttributes: PrivateKeyAttributesV2
    PrivateKeyFlags: PrivateKeyFlagsV2
    SubjectNameFlags: SubjectNameFlagsV2
    SupersededTemplates: Optional[List[str]] = None


class TemplateV3Output(BaseValidatorModel):
    CertificateValidity: CertificateValidity
    EnrollmentFlags: EnrollmentFlagsV3
    Extensions: ExtensionsV3Output
    GeneralFlags: GeneralFlagsV3
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3Output
    PrivateKeyFlags: PrivateKeyFlagsV3
    SubjectNameFlags: SubjectNameFlagsV3
    SupersededTemplates: Optional[List[str]] = None


class TemplateV3(BaseValidatorModel):
    CertificateValidity: CertificateValidity
    EnrollmentFlags: EnrollmentFlagsV3
    Extensions: ExtensionsV3
    GeneralFlags: GeneralFlagsV3
    HashAlgorithm: HashAlgorithmType
    PrivateKeyAttributes: PrivateKeyAttributesV3
    PrivateKeyFlags: PrivateKeyFlagsV3
    SubjectNameFlags: SubjectNameFlagsV3
    SupersededTemplates: Optional[List[str]] = None


class TemplateV4Output(BaseValidatorModel):
    CertificateValidity: CertificateValidity
    EnrollmentFlags: EnrollmentFlagsV4
    Extensions: ExtensionsV4Output
    GeneralFlags: GeneralFlagsV4
    PrivateKeyAttributes: PrivateKeyAttributesV4Output
    PrivateKeyFlags: PrivateKeyFlagsV4
    SubjectNameFlags: SubjectNameFlagsV4
    HashAlgorithm: Optional[HashAlgorithmType] = None
    SupersededTemplates: Optional[List[str]] = None


class TemplateV4(BaseValidatorModel):
    CertificateValidity: CertificateValidity
    EnrollmentFlags: EnrollmentFlagsV4
    Extensions: ExtensionsV4
    GeneralFlags: GeneralFlagsV4
    PrivateKeyAttributes: PrivateKeyAttributesV4
    PrivateKeyFlags: PrivateKeyFlagsV4
    SubjectNameFlags: SubjectNameFlagsV4
    HashAlgorithm: Optional[HashAlgorithmType] = None
    SupersededTemplates: Optional[List[str]] = None


class TemplateDefinitionOutput(BaseValidatorModel):
    TemplateV2: Optional[TemplateV2Output] = None
    TemplateV3: Optional[TemplateV3Output] = None
    TemplateV4: Optional[TemplateV4Output] = None


class TemplateDefinition(BaseValidatorModel):
    TemplateV2: Optional[TemplateV2] = None
    TemplateV3: Optional[TemplateV3] = None
    TemplateV4: Optional[TemplateV4] = None


class TemplateSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Definition: Optional[TemplateDefinitionOutput] = None
    Name: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicySchema: Optional[int] = None
    Revision: Optional[TemplateRevision] = None
    Status: Optional[TemplateStatusType] = None
    UpdatedAt: Optional[datetime] = None


class Template(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Definition: Optional[TemplateDefinitionOutput] = None
    Name: Optional[str] = None
    ObjectIdentifier: Optional[str] = None
    PolicySchema: Optional[int] = None
    Revision: Optional[TemplateRevision] = None
    Status: Optional[TemplateStatusType] = None
    UpdatedAt: Optional[datetime] = None

TemplateDefinitionUnion = Union[TemplateDefinition, TemplateDefinitionOutput]


# This class is the output for the 'list_templates' function.
class ListTemplatesResponse(BaseValidatorModel):
    Templates: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_template' function.
class GetTemplateResponse(BaseValidatorModel):
    Template: Template
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_template' function.
class CreateTemplateRequest(BaseValidatorModel):
    ConnectorArn: str
    Definition: TemplateDefinitionUnion
    Name: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_template' function.
class UpdateTemplateRequest(BaseValidatorModel):
    TemplateArn: str
    Definition: Optional[TemplateDefinitionUnion] = None
    ReenrollAllCertificateHolders: Optional[bool] = None