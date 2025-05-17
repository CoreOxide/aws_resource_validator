from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'associate_browser_settings' function.
class AssociateBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_data_protection_settings' function.
class AssociateDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str
    portalArn: str


# This class is the input for the 'associate_ip_access_settings' function.
class AssociateIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str


# This class is the input for the 'associate_network_settings' function.
class AssociateNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str


# This class is the input for the 'associate_trust_store' function.
class AssociateTrustStoreRequest(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str


# This class is the input for the 'associate_user_access_logging_settings' function.
class AssociateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str


# This class is the input for the 'associate_user_settings' function.
class AssociateUserSettingsRequest(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class BrowserSettingsSummary(BaseValidatorModel):
    browserSettingsArn: str


class BrowserSettings(BaseValidatorModel):
    browserSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    browserPolicy: Optional[str] = None
    customerManagedKey: Optional[str] = None


class CertificateSummary(BaseValidatorModel):
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None


class Certificate(BaseValidatorModel):
    body: Optional[bytes] = None
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None


class CookieSpecification(BaseValidatorModel):
    domain: str
    name: Optional[str] = None
    path: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class IpRule(BaseValidatorModel):
    ipRange: str
    description: Optional[str] = None


class CustomPattern(BaseValidatorModel):
    patternName: str
    patternRegex: str
    keywordRegex: Optional[str] = None
    patternDescription: Optional[str] = None


class DataProtectionSettingsSummary(BaseValidatorModel):
    dataProtectionSettingsArn: str
    creationDate: Optional[datetime] = None
    description: Optional[str] = None
    displayName: Optional[str] = None


class DeleteBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str


class DeleteDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str


class DeleteIdentityProviderRequest(BaseValidatorModel):
    identityProviderArn: str


class DeleteIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str


class DeleteNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str


class DeletePortalRequest(BaseValidatorModel):
    portalArn: str


class DeleteTrustStoreRequest(BaseValidatorModel):
    trustStoreArn: str


class DeleteUserAccessLoggingSettingsRequest(BaseValidatorModel):
    userAccessLoggingSettingsArn: str


class DeleteUserSettingsRequest(BaseValidatorModel):
    userSettingsArn: str


class DisassociateBrowserSettingsRequest(BaseValidatorModel):
    portalArn: str


class DisassociateDataProtectionSettingsRequest(BaseValidatorModel):
    portalArn: str


class DisassociateIpAccessSettingsRequest(BaseValidatorModel):
    portalArn: str


class DisassociateNetworkSettingsRequest(BaseValidatorModel):
    portalArn: str


class DisassociateTrustStoreRequest(BaseValidatorModel):
    portalArn: str


class DisassociateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    portalArn: str


class DisassociateUserSettingsRequest(BaseValidatorModel):
    portalArn: str


class ExpireSessionRequest(BaseValidatorModel):
    portalId: str
    sessionId: str


# This class is the input for the 'get_browser_settings' function.
class GetBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str


# This class is the input for the 'get_data_protection_settings' function.
class GetDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str


# This class is the input for the 'get_identity_provider' function.
class GetIdentityProviderRequest(BaseValidatorModel):
    identityProviderArn: str


class IdentityProvider(BaseValidatorModel):
    identityProviderArn: str
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


# This class is the input for the 'get_ip_access_settings' function.
class GetIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str


# This class is the input for the 'get_network_settings' function.
class GetNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str


class NetworkSettings(BaseValidatorModel):
    networkSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


# This class is the input for the 'get_portal' function.
class GetPortalRequest(BaseValidatorModel):
    portalArn: str


class Portal(BaseValidatorModel):
    portalArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    browserSettingsArn: Optional[str] = None
    browserType: Optional[Literal['Chrome']] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    dataProtectionSettingsArn: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    ipAccessSettingsArn: Optional[str] = None
    maxConcurrentSessions: Optional[int] = None
    networkSettingsArn: Optional[str] = None
    portalEndpoint: Optional[str] = None
    portalStatus: Optional[PortalStatusType] = None
    rendererType: Optional[Literal['AppStream']] = None
    statusReason: Optional[str] = None
    trustStoreArn: Optional[str] = None
    userAccessLoggingSettingsArn: Optional[str] = None
    userSettingsArn: Optional[str] = None


# This class is the input for the 'get_portal_service_provider_metadata' function.
class GetPortalServiceProviderMetadataRequest(BaseValidatorModel):
    portalArn: str


# This class is the input for the 'get_session' function.
class GetSessionRequest(BaseValidatorModel):
    portalId: str
    sessionId: str


class Session(BaseValidatorModel):
    clientIpAddresses: Optional[List[str]] = None
    endTime: Optional[datetime] = None
    portalArn: Optional[str] = None
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None


# This class is the input for the 'get_trust_store_certificate' function.
class GetTrustStoreCertificateRequest(BaseValidatorModel):
    thumbprint: str
    trustStoreArn: str


# This class is the input for the 'get_trust_store' function.
class GetTrustStoreRequest(BaseValidatorModel):
    trustStoreArn: str


class TrustStore(BaseValidatorModel):
    trustStoreArn: str
    associatedPortalArns: Optional[List[str]] = None


# This class is the input for the 'get_user_access_logging_settings' function.
class GetUserAccessLoggingSettingsRequest(BaseValidatorModel):
    userAccessLoggingSettingsArn: str


class UserAccessLoggingSettings(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    kinesisStreamArn: Optional[str] = None


# This class is the input for the 'get_user_settings' function.
class GetUserSettingsRequest(BaseValidatorModel):
    userSettingsArn: str


class IdentityProviderSummary(BaseValidatorModel):
    identityProviderArn: str
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


class RedactionPlaceHolder(BaseValidatorModel):
    redactionPlaceHolderType: Literal['CustomText']
    redactionPlaceHolderText: Optional[str] = None


class IpAccessSettingsSummary(BaseValidatorModel):
    ipAccessSettingsArn: str
    creationDate: Optional[datetime] = None
    description: Optional[str] = None
    displayName: Optional[str] = None


# This class is the input for the 'list_browser_settings' function.
class ListBrowserSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_data_protection_settings' function.
class ListDataProtectionSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_identity_providers' function.
class ListIdentityProvidersRequest(BaseValidatorModel):
    portalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_ip_access_settings' function.
class ListIpAccessSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_network_settings' function.
class ListNetworkSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NetworkSettingsSummary(BaseValidatorModel):
    networkSettingsArn: str
    vpcId: Optional[str] = None


# This class is the input for the 'list_portals' function.
class ListPortalsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PortalSummary(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    browserSettingsArn: Optional[str] = None
    browserType: Optional[Literal['Chrome']] = None
    creationDate: Optional[datetime] = None
    dataProtectionSettingsArn: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    ipAccessSettingsArn: Optional[str] = None
    maxConcurrentSessions: Optional[int] = None
    networkSettingsArn: Optional[str] = None
    portalEndpoint: Optional[str] = None
    portalStatus: Optional[PortalStatusType] = None
    rendererType: Optional[Literal['AppStream']] = None
    trustStoreArn: Optional[str] = None
    userAccessLoggingSettingsArn: Optional[str] = None
    userSettingsArn: Optional[str] = None


# This class is the input for the 'list_sessions' function.
class ListSessionsRequest(BaseValidatorModel):
    portalId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sessionId: Optional[str] = None
    sortBy: Optional[SessionSortByType] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None


class SessionSummary(BaseValidatorModel):
    endTime: Optional[datetime] = None
    portalArn: Optional[str] = None
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_trust_store_certificates' function.
class ListTrustStoreCertificatesRequest(BaseValidatorModel):
    trustStoreArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_trust_stores' function.
class ListTrustStoresRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TrustStoreSummary(BaseValidatorModel):
    trustStoreArn: Optional[str] = None


# This class is the input for the 'list_user_access_logging_settings' function.
class ListUserAccessLoggingSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class UserAccessLoggingSettingsSummary(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: Optional[str] = None


# This class is the input for the 'list_user_settings' function.
class ListUserSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ToolbarConfigurationOutput(BaseValidatorModel):
    hiddenToolbarItems: Optional[List[ToolbarItemType]] = None
    maxDisplayResolution: Optional[MaxDisplayResolutionType] = None
    toolbarType: Optional[ToolbarTypeType] = None
    visualMode: Optional[VisualModeType] = None


class ToolbarConfiguration(BaseValidatorModel):
    hiddenToolbarItems: Optional[List[ToolbarItemType]] = None
    maxDisplayResolution: Optional[MaxDisplayResolutionType] = None
    toolbarType: Optional[ToolbarTypeType] = None
    visualMode: Optional[VisualModeType] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_browser_settings' function.
class UpdateBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str
    browserPolicy: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_identity_provider' function.
class UpdateIdentityProviderRequest(BaseValidatorModel):
    identityProviderArn: str
    clientToken: Optional[str] = None
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


# This class is the input for the 'update_network_settings' function.
class UpdateNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


# This class is the input for the 'update_portal' function.
class UpdatePortalRequest(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None


# This class is the input for the 'update_user_access_logging_settings' function.
class UpdateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    clientToken: Optional[str] = None
    kinesisStreamArn: Optional[str] = None


# This class is the output for the 'associate_browser_settings' function.
class AssociateBrowserSettingsResponse(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_data_protection_settings' function.
class AssociateDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_ip_access_settings' function.
class AssociateIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_network_settings' function.
class AssociateNetworkSettingsResponse(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_trust_store' function.
class AssociateTrustStoreResponse(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_user_access_logging_settings' function.
class AssociateUserAccessLoggingSettingsResponse(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_user_settings' function.
class AssociateUserSettingsResponse(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_browser_settings' function.
class CreateBrowserSettingsResponse(BaseValidatorModel):
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_protection_settings' function.
class CreateDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_identity_provider' function.
class CreateIdentityProviderResponse(BaseValidatorModel):
    identityProviderArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ip_access_settings' function.
class CreateIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_network_settings' function.
class CreateNetworkSettingsResponse(BaseValidatorModel):
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_portal' function.
class CreatePortalResponse(BaseValidatorModel):
    portalArn: str
    portalEndpoint: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_trust_store' function.
class CreateTrustStoreResponse(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user_access_logging_settings' function.
class CreateUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user_settings' function.
class CreateUserSettingsResponse(BaseValidatorModel):
    userSettingsArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_portal_service_provider_metadata' function.
class GetPortalServiceProviderMetadataResponse(BaseValidatorModel):
    portalArn: str
    serviceProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trust_store' function.
class UpdateTrustStoreResponse(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_trust_store' function.
class UpdateTrustStoreRequest(BaseValidatorModel):
    trustStoreArn: str
    certificatesToAdd: Optional[List[Blob]] = None
    certificatesToDelete: Optional[List[str]] = None
    clientToken: Optional[str] = None


# This class is the output for the 'list_browser_settings' function.
class ListBrowserSettingsResponse(BaseValidatorModel):
    browserSettings: List[BrowserSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_browser_settings' function.
class GetBrowserSettingsResponse(BaseValidatorModel):
    browserSettings: BrowserSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_browser_settings' function.
class UpdateBrowserSettingsResponse(BaseValidatorModel):
    browserSettings: BrowserSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_trust_store_certificates' function.
class ListTrustStoreCertificatesResponse(BaseValidatorModel):
    certificateList: List[CertificateSummary]
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_trust_store_certificate' function.
class GetTrustStoreCertificateResponse(BaseValidatorModel):
    certificate: Certificate
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


class CookieSynchronizationConfigurationOutput(BaseValidatorModel):
    allowlist: List[CookieSpecification]
    blocklist: Optional[List[CookieSpecification]] = None


class CookieSynchronizationConfiguration(BaseValidatorModel):
    allowlist: List[CookieSpecification]
    blocklist: Optional[List[CookieSpecification]] = None


# This class is the input for the 'create_browser_settings' function.
class CreateBrowserSettingsRequest(BaseValidatorModel):
    browserPolicy: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_identity_provider' function.
class CreateIdentityProviderRequest(BaseValidatorModel):
    identityProviderDetails: Dict[str, str]
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    portalArn: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_network_settings' function.
class CreateNetworkSettingsRequest(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_portal' function.
class CreatePortalRequest(BaseValidatorModel):
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_trust_store' function.
class CreateTrustStoreRequest(BaseValidatorModel):
    certificateList: List[Blob]
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_user_access_logging_settings' function.
class CreateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    kinesisStreamArn: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]
    clientToken: Optional[str] = None


# This class is the input for the 'create_ip_access_settings' function.
class CreateIpAccessSettingsRequest(BaseValidatorModel):
    ipRules: List[IpRule]
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    tags: Optional[List[Tag]] = None


class IpAccessSettings(BaseValidatorModel):
    ipAccessSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[List[IpRule]] = None


# This class is the input for the 'update_ip_access_settings' function.
class UpdateIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[List[IpRule]] = None


# This class is the output for the 'list_data_protection_settings' function.
class ListDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettings: List[DataProtectionSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_identity_provider' function.
class GetIdentityProviderResponse(BaseValidatorModel):
    identityProvider: IdentityProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_identity_provider' function.
class UpdateIdentityProviderResponse(BaseValidatorModel):
    identityProvider: IdentityProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_network_settings' function.
class GetNetworkSettingsResponse(BaseValidatorModel):
    networkSettings: NetworkSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_network_settings' function.
class UpdateNetworkSettingsResponse(BaseValidatorModel):
    networkSettings: NetworkSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_portal' function.
class GetPortalResponse(BaseValidatorModel):
    portal: Portal
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_portal' function.
class UpdatePortalResponse(BaseValidatorModel):
    portal: Portal
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_session' function.
class GetSessionResponse(BaseValidatorModel):
    session: Session
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_trust_store' function.
class GetTrustStoreResponse(BaseValidatorModel):
    trustStore: TrustStore
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user_access_logging_settings' function.
class GetUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user_access_logging_settings' function.
class UpdateUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_identity_providers' function.
class ListIdentityProvidersResponse(BaseValidatorModel):
    identityProviders: List[IdentityProviderSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InlineRedactionPatternOutput(BaseValidatorModel):
    redactionPlaceHolder: RedactionPlaceHolder
    builtInPatternId: Optional[str] = None
    confidenceLevel: Optional[int] = None
    customPattern: Optional[CustomPattern] = None
    enforcedUrls: Optional[List[str]] = None
    exemptUrls: Optional[List[str]] = None


class InlineRedactionPattern(BaseValidatorModel):
    redactionPlaceHolder: RedactionPlaceHolder
    builtInPatternId: Optional[str] = None
    confidenceLevel: Optional[int] = None
    customPattern: Optional[CustomPattern] = None
    enforcedUrls: Optional[List[str]] = None
    exemptUrls: Optional[List[str]] = None


# This class is the output for the 'list_ip_access_settings' function.
class ListIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettings: List[IpAccessSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDataProtectionSettingsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSessionsRequestPaginate(BaseValidatorModel):
    portalId: str
    sessionId: Optional[str] = None
    sortBy: Optional[SessionSortByType] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_network_settings' function.
class ListNetworkSettingsResponse(BaseValidatorModel):
    networkSettings: List[NetworkSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_portals' function.
class ListPortalsResponse(BaseValidatorModel):
    portals: List[PortalSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sessions' function.
class ListSessionsResponse(BaseValidatorModel):
    sessions: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_trust_stores' function.
class ListTrustStoresResponse(BaseValidatorModel):
    trustStores: List[TrustStoreSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_user_access_logging_settings' function.
class ListUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettings: List[UserAccessLoggingSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ToolbarConfigurationUnion = Union[ToolbarConfiguration, ToolbarConfigurationOutput]


class UserSettingsSummary(BaseValidatorModel):
    userSettingsArn: str
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationOutput] = None
    copyAllowed: Optional[EnabledTypeType] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    toolbarConfiguration: Optional[ToolbarConfigurationOutput] = None
    uploadAllowed: Optional[EnabledTypeType] = None


class UserSettings(BaseValidatorModel):
    userSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationOutput] = None
    copyAllowed: Optional[EnabledTypeType] = None
    customerManagedKey: Optional[str] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    toolbarConfiguration: Optional[ToolbarConfigurationOutput] = None
    uploadAllowed: Optional[EnabledTypeType] = None

CookieSynchronizationConfigurationUnion = Union[CookieSynchronizationConfiguration, CookieSynchronizationConfigurationOutput]


# This class is the output for the 'get_ip_access_settings' function.
class GetIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettings: IpAccessSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ip_access_settings' function.
class UpdateIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettings: IpAccessSettings
    ResponseMetadata: ResponseMetadata


class InlineRedactionConfigurationOutput(BaseValidatorModel):
    inlineRedactionPatterns: List[InlineRedactionPatternOutput]
    globalConfidenceLevel: Optional[int] = None
    globalEnforcedUrls: Optional[List[str]] = None
    globalExemptUrls: Optional[List[str]] = None


class InlineRedactionConfiguration(BaseValidatorModel):
    inlineRedactionPatterns: List[InlineRedactionPattern]
    globalConfidenceLevel: Optional[int] = None
    globalEnforcedUrls: Optional[List[str]] = None
    globalExemptUrls: Optional[List[str]] = None


# This class is the output for the 'list_user_settings' function.
class ListUserSettingsResponse(BaseValidatorModel):
    userSettings: List[UserSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_user_settings' function.
class GetUserSettingsResponse(BaseValidatorModel):
    userSettings: UserSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user_settings' function.
class UpdateUserSettingsResponse(BaseValidatorModel):
    userSettings: UserSettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_user_settings' function.
class CreateUserSettingsRequest(BaseValidatorModel):
    copyAllowed: EnabledTypeType
    downloadAllowed: EnabledTypeType
    pasteAllowed: EnabledTypeType
    printAllowed: EnabledTypeType
    uploadAllowed: EnabledTypeType
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationUnion] = None
    customerManagedKey: Optional[str] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    tags: Optional[List[Tag]] = None
    toolbarConfiguration: Optional[ToolbarConfigurationUnion] = None


# This class is the input for the 'update_user_settings' function.
class UpdateUserSettingsRequest(BaseValidatorModel):
    userSettingsArn: str
    clientToken: Optional[str] = None
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationUnion] = None
    copyAllowed: Optional[EnabledTypeType] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    toolbarConfiguration: Optional[ToolbarConfigurationUnion] = None
    uploadAllowed: Optional[EnabledTypeType] = None


class DataProtectionSettings(BaseValidatorModel):
    dataProtectionSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationOutput] = None

InlineRedactionConfigurationUnion = Union[InlineRedactionConfiguration, InlineRedactionConfigurationOutput]


# This class is the output for the 'get_data_protection_settings' function.
class GetDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettings: DataProtectionSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_data_protection_settings' function.
class UpdateDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettings: DataProtectionSettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_data_protection_settings' function.
class CreateDataProtectionSettingsRequest(BaseValidatorModel):
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationUnion] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_data_protection_settings' function.
class UpdateDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationUnion] = None