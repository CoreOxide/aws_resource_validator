from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str
    portalArn: str


class AssociateIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str


class AssociateNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str


class AssociateTrustStoreRequest(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str


class AssociateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str


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


class GetBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str


class GetDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str


class GetIdentityProviderRequest(BaseValidatorModel):
    identityProviderArn: str


class IdentityProvider(BaseValidatorModel):
    identityProviderArn: str
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


class GetIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str


class GetNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str


class NetworkSettings(BaseValidatorModel):
    networkSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


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


class GetPortalServiceProviderMetadataRequest(BaseValidatorModel):
    portalArn: str


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


class GetTrustStoreCertificateRequest(BaseValidatorModel):
    thumbprint: str
    trustStoreArn: str


class GetTrustStoreRequest(BaseValidatorModel):
    trustStoreArn: str


class TrustStore(BaseValidatorModel):
    trustStoreArn: str
    associatedPortalArns: Optional[List[str]] = None


class GetUserAccessLoggingSettingsRequest(BaseValidatorModel):
    userAccessLoggingSettingsArn: str


class UserAccessLoggingSettings(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    kinesisStreamArn: Optional[str] = None


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


class ListBrowserSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDataProtectionSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdentityProvidersRequest(BaseValidatorModel):
    portalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIpAccessSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListNetworkSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NetworkSettingsSummary(BaseValidatorModel):
    networkSettingsArn: str
    vpcId: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTrustStoreCertificatesRequest(BaseValidatorModel):
    trustStoreArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTrustStoresRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TrustStoreSummary(BaseValidatorModel):
    trustStoreArn: Optional[str] = None


class ListUserAccessLoggingSettingsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class UserAccessLoggingSettingsSummary(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: Optional[str] = None


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


class UpdateBrowserSettingsRequest(BaseValidatorModel):
    browserSettingsArn: str
    browserPolicy: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateIdentityProviderRequest(BaseValidatorModel):
    identityProviderArn: str
    clientToken: Optional[str] = None
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


class UpdateNetworkSettingsRequest(BaseValidatorModel):
    networkSettingsArn: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


class UpdatePortalRequest(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None


class UpdateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    clientToken: Optional[str] = None
    kinesisStreamArn: Optional[str] = None


class AssociateBrowserSettingsResponse(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


class AssociateDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


class AssociateIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


class AssociateNetworkSettingsResponse(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadata


class AssociateTrustStoreResponse(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


class AssociateUserAccessLoggingSettingsResponse(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadata


class AssociateUserSettingsResponse(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str
    ResponseMetadata: ResponseMetadata


class CreateBrowserSettingsResponse(BaseValidatorModel):
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadata


class CreateDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettingsArn: str
    ResponseMetadata: ResponseMetadata


class CreateIdentityProviderResponse(BaseValidatorModel):
    identityProviderArn: str
    ResponseMetadata: ResponseMetadata


class CreateIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadata


class CreateNetworkSettingsResponse(BaseValidatorModel):
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadata


class CreatePortalResponse(BaseValidatorModel):
    portalArn: str
    portalEndpoint: str
    ResponseMetadata: ResponseMetadata


class CreateTrustStoreResponse(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


class CreateUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadata


class CreateUserSettingsResponse(BaseValidatorModel):
    userSettingsArn: str
    ResponseMetadata: ResponseMetadata


class GetPortalServiceProviderMetadataResponse(BaseValidatorModel):
    portalArn: str
    serviceProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadata


class UpdateTrustStoreResponse(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata


class UpdateTrustStoreRequest(BaseValidatorModel):
    trustStoreArn: str
    certificatesToAdd: Optional[List[Blob]] = None
    certificatesToDelete: Optional[List[str]] = None
    clientToken: Optional[str] = None


class ListBrowserSettingsResponse(BaseValidatorModel):
    browserSettings: List[BrowserSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetBrowserSettingsResponse(BaseValidatorModel):
    browserSettings: BrowserSettings
    ResponseMetadata: ResponseMetadata


class UpdateBrowserSettingsResponse(BaseValidatorModel):
    browserSettings: BrowserSettings
    ResponseMetadata: ResponseMetadata


class ListTrustStoreCertificatesResponse(BaseValidatorModel):
    certificateList: List[CertificateSummary]
    trustStoreArn: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class CreateBrowserSettingsRequest(BaseValidatorModel):
    browserPolicy: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateIdentityProviderRequest(BaseValidatorModel):
    identityProviderDetails: Dict[str, str]
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    portalArn: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateNetworkSettingsRequest(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreatePortalRequest(BaseValidatorModel):
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None
    tags: Optional[List[Tag]] = None


class CreateTrustStoreRequest(BaseValidatorModel):
    certificateList: List[Blob]
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateUserAccessLoggingSettingsRequest(BaseValidatorModel):
    kinesisStreamArn: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]
    clientToken: Optional[str] = None


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


class UpdateIpAccessSettingsRequest(BaseValidatorModel):
    ipAccessSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[List[IpRule]] = None


class ListDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettings: List[DataProtectionSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetIdentityProviderResponse(BaseValidatorModel):
    identityProvider: IdentityProvider
    ResponseMetadata: ResponseMetadata


class UpdateIdentityProviderResponse(BaseValidatorModel):
    identityProvider: IdentityProvider
    ResponseMetadata: ResponseMetadata


class GetNetworkSettingsResponse(BaseValidatorModel):
    networkSettings: NetworkSettings
    ResponseMetadata: ResponseMetadata


class UpdateNetworkSettingsResponse(BaseValidatorModel):
    networkSettings: NetworkSettings
    ResponseMetadata: ResponseMetadata


class GetPortalResponse(BaseValidatorModel):
    portal: Portal
    ResponseMetadata: ResponseMetadata


class UpdatePortalResponse(BaseValidatorModel):
    portal: Portal
    ResponseMetadata: ResponseMetadata


class GetSessionResponse(BaseValidatorModel):
    session: Session
    ResponseMetadata: ResponseMetadata


class GetTrustStoreResponse(BaseValidatorModel):
    trustStore: TrustStore
    ResponseMetadata: ResponseMetadata


class GetUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettings
    ResponseMetadata: ResponseMetadata


class UpdateUserAccessLoggingSettingsResponse(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettings
    ResponseMetadata: ResponseMetadata


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


class ListNetworkSettingsResponse(BaseValidatorModel):
    networkSettings: List[NetworkSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPortalsResponse(BaseValidatorModel):
    portals: List[PortalSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSessionsResponse(BaseValidatorModel):
    sessions: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTrustStoresResponse(BaseValidatorModel):
    trustStores: List[TrustStoreSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class GetIpAccessSettingsResponse(BaseValidatorModel):
    ipAccessSettings: IpAccessSettings
    ResponseMetadata: ResponseMetadata


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


class ListUserSettingsResponse(BaseValidatorModel):
    userSettings: List[UserSettingsSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetUserSettingsResponse(BaseValidatorModel):
    userSettings: UserSettings
    ResponseMetadata: ResponseMetadata


class UpdateUserSettingsResponse(BaseValidatorModel):
    userSettings: UserSettings
    ResponseMetadata: ResponseMetadata


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


class GetDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettings: DataProtectionSettings
    ResponseMetadata: ResponseMetadata


class UpdateDataProtectionSettingsResponse(BaseValidatorModel):
    dataProtectionSettings: DataProtectionSettings
    ResponseMetadata: ResponseMetadata


class CreateDataProtectionSettingsRequest(BaseValidatorModel):
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationUnion] = None
    tags: Optional[List[Tag]] = None


class UpdateDataProtectionSettingsRequest(BaseValidatorModel):
    dataProtectionSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationUnion] = None