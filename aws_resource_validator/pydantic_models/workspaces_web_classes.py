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
from aws_resource_validator.pydantic_models.workspaces_web_constants import *

class AssociateBrowserSettingsRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str
    portalArn: str


class AssociateIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str


class AssociateNetworkSettingsRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str


class AssociateTrustStoreRequestTypeDef(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str


class AssociateUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str


class AssociateUserSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str


class BrowserSettingsSummaryTypeDef(BaseValidatorModel):
    browserSettingsArn: str


class BrowserSettingsTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    browserPolicy: Optional[str] = None
    customerManagedKey: Optional[str] = None


class CertificateSummaryTypeDef(BaseValidatorModel):
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None


class CertificateTypeDef(BaseValidatorModel):
    body: Optional[bytes] = None
    issuer: Optional[str] = None
    notValidAfter: Optional[datetime] = None
    notValidBefore: Optional[datetime] = None
    subject: Optional[str] = None
    thumbprint: Optional[str] = None


class CookieSpecificationTypeDef(BaseValidatorModel):
    domain: str
    name: Optional[str] = None
    path: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class IpRuleTypeDef(BaseValidatorModel):
    ipRange: str
    description: Optional[str] = None


class CustomPatternTypeDef(BaseValidatorModel):
    patternName: str
    patternRegex: str
    keywordRegex: Optional[str] = None
    patternDescription: Optional[str] = None


class DataProtectionSettingsSummaryTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str
    creationDate: Optional[datetime] = None
    description: Optional[str] = None
    displayName: Optional[str] = None


class DeleteBrowserSettingsRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str


class DeleteDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str


class DeleteIdentityProviderRequestTypeDef(BaseValidatorModel):
    identityProviderArn: str


class DeleteIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str


class DeleteNetworkSettingsRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str


class DeletePortalRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DeleteTrustStoreRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str


class DeleteUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str


class DeleteUserSettingsRequestTypeDef(BaseValidatorModel):
    userSettingsArn: str


class DisassociateBrowserSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DisassociateDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DisassociateIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DisassociateNetworkSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DisassociateTrustStoreRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DisassociateUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str


class DisassociateUserSettingsRequestTypeDef(BaseValidatorModel):
    portalArn: str


class ExpireSessionRequestTypeDef(BaseValidatorModel):
    portalId: str
    sessionId: str


class GetBrowserSettingsRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str


class GetDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str


class GetIdentityProviderRequestTypeDef(BaseValidatorModel):
    identityProviderArn: str


class IdentityProviderTypeDef(BaseValidatorModel):
    identityProviderArn: str
    identityProviderDetails: Optional[Dict[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


class GetIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str


class GetNetworkSettingsRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str


class NetworkSettingsTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None


class GetPortalRequestTypeDef(BaseValidatorModel):
    portalArn: str


class PortalTypeDef(BaseValidatorModel):
    portalArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    browserSettingsArn: Optional[str] = None
    browserType: Optional[Literal["Chrome"]] = None
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
    rendererType: Optional[Literal["AppStream"]] = None
    statusReason: Optional[str] = None
    trustStoreArn: Optional[str] = None
    userAccessLoggingSettingsArn: Optional[str] = None
    userSettingsArn: Optional[str] = None


class GetPortalServiceProviderMetadataRequestTypeDef(BaseValidatorModel):
    portalArn: str


class GetSessionRequestTypeDef(BaseValidatorModel):
    portalId: str
    sessionId: str


class SessionTypeDef(BaseValidatorModel):
    clientIpAddresses: Optional[List[str]] = None
    endTime: Optional[datetime] = None
    portalArn: Optional[str] = None
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None


class GetTrustStoreCertificateRequestTypeDef(BaseValidatorModel):
    thumbprint: str
    trustStoreArn: str


class GetTrustStoreRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str


class TrustStoreTypeDef(BaseValidatorModel):
    trustStoreArn: str
    associatedPortalArns: Optional[List[str]] = None


class GetUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str


class UserAccessLoggingSettingsTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    associatedPortalArns: Optional[List[str]] = None
    kinesisStreamArn: Optional[str] = None


class GetUserSettingsRequestTypeDef(BaseValidatorModel):
    userSettingsArn: str


class IdentityProviderSummaryTypeDef(BaseValidatorModel):
    identityProviderArn: str
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


class RedactionPlaceHolderTypeDef(BaseValidatorModel):
    redactionPlaceHolderType: Literal["CustomText"]
    redactionPlaceHolderText: Optional[str] = None


class IpAccessSettingsSummaryTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    creationDate: Optional[datetime] = None
    description: Optional[str] = None
    displayName: Optional[str] = None


class ListBrowserSettingsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdentityProvidersRequestTypeDef(BaseValidatorModel):
    portalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListNetworkSettingsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NetworkSettingsSummaryTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    vpcId: Optional[str] = None


class ListPortalsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PortalSummaryTypeDef(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    browserSettingsArn: Optional[str] = None
    browserType: Optional[Literal["Chrome"]] = None
    creationDate: Optional[datetime] = None
    dataProtectionSettingsArn: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    ipAccessSettingsArn: Optional[str] = None
    maxConcurrentSessions: Optional[int] = None
    networkSettingsArn: Optional[str] = None
    portalEndpoint: Optional[str] = None
    portalStatus: Optional[PortalStatusType] = None
    rendererType: Optional[Literal["AppStream"]] = None
    trustStoreArn: Optional[str] = None
    userAccessLoggingSettingsArn: Optional[str] = None
    userSettingsArn: Optional[str] = None


class ListSessionsRequestTypeDef(BaseValidatorModel):
    portalId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sessionId: Optional[str] = None
    sortBy: Optional[SessionSortByType] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None


class SessionSummaryTypeDef(BaseValidatorModel):
    endTime: Optional[datetime] = None
    portalArn: Optional[str] = None
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTrustStoreCertificatesRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTrustStoresRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TrustStoreSummaryTypeDef(BaseValidatorModel):
    trustStoreArn: Optional[str] = None


class ListUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class UserAccessLoggingSettingsSummaryTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    kinesisStreamArn: Optional[str] = None


class ListUserSettingsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ToolbarConfigurationOutputTypeDef(BaseValidatorModel):
    hiddenToolbarItems: Optional[List[ToolbarItemType]] = None
    maxDisplayResolution: Optional[MaxDisplayResolutionType] = None
    toolbarType: Optional[ToolbarTypeType] = None
    visualMode: Optional[VisualModeType] = None


class ToolbarConfigurationTypeDef(BaseValidatorModel):
    hiddenToolbarItems: Optional[Sequence[ToolbarItemType]] = None
    maxDisplayResolution: Optional[MaxDisplayResolutionType] = None
    toolbarType: Optional[ToolbarTypeType] = None
    visualMode: Optional[VisualModeType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateBrowserSettingsRequestTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    browserPolicy: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateIdentityProviderRequestTypeDef(BaseValidatorModel):
    identityProviderArn: str
    clientToken: Optional[str] = None
    identityProviderDetails: Optional[Mapping[str, str]] = None
    identityProviderName: Optional[str] = None
    identityProviderType: Optional[IdentityProviderTypeType] = None


class UpdateNetworkSettingsRequestTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetIds: Optional[Sequence[str]] = None
    vpcId: Optional[str] = None


class UpdatePortalRequestTypeDef(BaseValidatorModel):
    portalArn: str
    authenticationType: Optional[AuthenticationTypeType] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None


class UpdateUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    clientToken: Optional[str] = None
    kinesisStreamArn: Optional[str] = None


class AssociateBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateDataProtectionSettingsResponseTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    portalArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateTrustStoreResponseTypeDef(BaseValidatorModel):
    portalArn: str
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    portalArn: str
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateUserSettingsResponseTypeDef(BaseValidatorModel):
    portalArn: str
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataProtectionSettingsResponseTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIdentityProviderResponseTypeDef(BaseValidatorModel):
    identityProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePortalResponseTypeDef(BaseValidatorModel):
    portalArn: str
    portalEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrustStoreResponseTypeDef(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettingsArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPortalServiceProviderMetadataResponseTypeDef(BaseValidatorModel):
    portalArn: str
    serviceProviderSamlMetadata: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTrustStoreResponseTypeDef(BaseValidatorModel):
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class UpdateTrustStoreRequestTypeDef(BaseValidatorModel):
    trustStoreArn: str
    certificatesToAdd: Optional[Sequence[BlobTypeDef]] = None
    certificatesToDelete: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None


class ListBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettings: List[BrowserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBrowserSettingsResponseTypeDef(BaseValidatorModel):
    browserSettings: BrowserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTrustStoreCertificatesResponseTypeDef(BaseValidatorModel):
    certificateList: List[CertificateSummaryTypeDef]
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetTrustStoreCertificateResponseTypeDef(BaseValidatorModel):
    certificate: CertificateTypeDef
    trustStoreArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CookieSynchronizationConfigurationOutputTypeDef(BaseValidatorModel):
    allowlist: List[CookieSpecificationTypeDef]
    blocklist: Optional[List[CookieSpecificationTypeDef]] = None


class CookieSynchronizationConfigurationTypeDef(BaseValidatorModel):
    allowlist: Sequence[CookieSpecificationTypeDef]
    blocklist: Optional[Sequence[CookieSpecificationTypeDef]] = None


class CreateBrowserSettingsRequestTypeDef(BaseValidatorModel):
    browserPolicy: str
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateIdentityProviderRequestTypeDef(BaseValidatorModel):
    identityProviderDetails: Mapping[str, str]
    identityProviderName: str
    identityProviderType: IdentityProviderTypeType
    portalArn: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateNetworkSettingsRequestTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreatePortalRequestTypeDef(BaseValidatorModel):
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    displayName: Optional[str] = None
    instanceType: Optional[InstanceTypeType] = None
    maxConcurrentSessions: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateTrustStoreRequestTypeDef(BaseValidatorModel):
    certificateList: Sequence[BlobTypeDef]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateUserAccessLoggingSettingsRequestTypeDef(BaseValidatorModel):
    kinesisStreamArn: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]
    clientToken: Optional[str] = None


class CreateIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    ipRules: Sequence[IpRuleTypeDef]
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class IpAccessSettingsTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[List[IpRuleTypeDef]] = None


class UpdateIpAccessSettingsRequestTypeDef(BaseValidatorModel):
    ipAccessSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    ipRules: Optional[Sequence[IpRuleTypeDef]] = None


class ListDataProtectionSettingsResponseTypeDef(BaseValidatorModel):
    dataProtectionSettings: List[DataProtectionSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetIdentityProviderResponseTypeDef(BaseValidatorModel):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIdentityProviderResponseTypeDef(BaseValidatorModel):
    identityProvider: IdentityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettings: NetworkSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPortalResponseTypeDef(BaseValidatorModel):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePortalResponseTypeDef(BaseValidatorModel):
    portal: PortalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSessionResponseTypeDef(BaseValidatorModel):
    session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrustStoreResponseTypeDef(BaseValidatorModel):
    trustStore: TrustStoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettings: UserAccessLoggingSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListIdentityProvidersResponseTypeDef(BaseValidatorModel):
    identityProviders: List[IdentityProviderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InlineRedactionPatternOutputTypeDef(BaseValidatorModel):
    redactionPlaceHolder: RedactionPlaceHolderTypeDef
    builtInPatternId: Optional[str] = None
    confidenceLevel: Optional[int] = None
    customPattern: Optional[CustomPatternTypeDef] = None
    enforcedUrls: Optional[List[str]] = None
    exemptUrls: Optional[List[str]] = None


class InlineRedactionPatternTypeDef(BaseValidatorModel):
    redactionPlaceHolder: RedactionPlaceHolderTypeDef
    builtInPatternId: Optional[str] = None
    confidenceLevel: Optional[int] = None
    customPattern: Optional[CustomPatternTypeDef] = None
    enforcedUrls: Optional[Sequence[str]] = None
    exemptUrls: Optional[Sequence[str]] = None


class ListIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettings: List[IpAccessSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDataProtectionSettingsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSessionsRequestPaginateTypeDef(BaseValidatorModel):
    portalId: str
    sessionId: Optional[str] = None
    sortBy: Optional[SessionSortByType] = None
    status: Optional[SessionStatusType] = None
    username: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNetworkSettingsResponseTypeDef(BaseValidatorModel):
    networkSettings: List[NetworkSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPortalsResponseTypeDef(BaseValidatorModel):
    portals: List[PortalSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSessionsResponseTypeDef(BaseValidatorModel):
    sessions: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTrustStoresResponseTypeDef(BaseValidatorModel):
    trustStores: List[TrustStoreSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListUserAccessLoggingSettingsResponseTypeDef(BaseValidatorModel):
    userAccessLoggingSettings: List[UserAccessLoggingSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UserSettingsSummaryTypeDef(BaseValidatorModel):
    userSettingsArn: str
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationOutputTypeDef] = None
    copyAllowed: Optional[EnabledTypeType] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    toolbarConfiguration: Optional[ToolbarConfigurationOutputTypeDef] = None
    uploadAllowed: Optional[EnabledTypeType] = None


class UserSettingsTypeDef(BaseValidatorModel):
    userSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationOutputTypeDef] = None
    copyAllowed: Optional[EnabledTypeType] = None
    customerManagedKey: Optional[str] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    toolbarConfiguration: Optional[ToolbarConfigurationOutputTypeDef] = None
    uploadAllowed: Optional[EnabledTypeType] = None


class GetIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIpAccessSettingsResponseTypeDef(BaseValidatorModel):
    ipAccessSettings: IpAccessSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InlineRedactionConfigurationOutputTypeDef(BaseValidatorModel):
    inlineRedactionPatterns: List[InlineRedactionPatternOutputTypeDef]
    globalConfidenceLevel: Optional[int] = None
    globalEnforcedUrls: Optional[List[str]] = None
    globalExemptUrls: Optional[List[str]] = None


class InlineRedactionConfigurationTypeDef(BaseValidatorModel):
    inlineRedactionPatterns: Sequence[InlineRedactionPatternTypeDef]
    globalConfidenceLevel: Optional[int] = None
    globalEnforcedUrls: Optional[Sequence[str]] = None
    globalExemptUrls: Optional[Sequence[str]] = None


class ListUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettings: List[UserSettingsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserSettingsResponseTypeDef(BaseValidatorModel):
    userSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ToolbarConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CookieSynchronizationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateUserSettingsRequestTypeDef(BaseValidatorModel):
    copyAllowed: EnabledTypeType
    downloadAllowed: EnabledTypeType
    pasteAllowed: EnabledTypeType
    printAllowed: EnabledTypeType
    uploadAllowed: EnabledTypeType
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationUnionTypeDef] = None
    customerManagedKey: Optional[str] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    toolbarConfiguration: Optional[ToolbarConfigurationUnionTypeDef] = None


class UpdateUserSettingsRequestTypeDef(BaseValidatorModel):
    userSettingsArn: str
    clientToken: Optional[str] = None
    cookieSynchronizationConfiguration: Optional[CookieSynchronizationConfigurationUnionTypeDef] = None
    copyAllowed: Optional[EnabledTypeType] = None
    deepLinkAllowed: Optional[EnabledTypeType] = None
    disconnectTimeoutInMinutes: Optional[int] = None
    downloadAllowed: Optional[EnabledTypeType] = None
    idleDisconnectTimeoutInMinutes: Optional[int] = None
    pasteAllowed: Optional[EnabledTypeType] = None
    printAllowed: Optional[EnabledTypeType] = None
    toolbarConfiguration: Optional[ToolbarConfigurationUnionTypeDef] = None
    uploadAllowed: Optional[EnabledTypeType] = None


class DataProtectionSettingsTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str
    additionalEncryptionContext: Optional[Dict[str, str]] = None
    associatedPortalArns: Optional[List[str]] = None
    creationDate: Optional[datetime] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationOutputTypeDef] = None


class GetDataProtectionSettingsResponseTypeDef(BaseValidatorModel):
    dataProtectionSettings: DataProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataProtectionSettingsResponseTypeDef(BaseValidatorModel):
    dataProtectionSettings: DataProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InlineRedactionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    additionalEncryptionContext: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None
    customerManagedKey: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDataProtectionSettingsRequestTypeDef(BaseValidatorModel):
    dataProtectionSettingsArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    inlineRedactionConfiguration: Optional[InlineRedactionConfigurationUnionTypeDef] = None


